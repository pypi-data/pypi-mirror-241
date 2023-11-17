import time
import os
import tempfile
import cv2
import torch.multiprocessing as multiprocessing
import subprocess as sp

from .net import Net, remove_many
from ..error import ToolsRuntimeError, ToolsTimeoutError, ToolsValueError


def _deal_frames(input_path, model_name, total_frames, results_dict, error_dict):
    _video = None
    _index = 0
    try:
        print('transparent background start...')
        _video = cv2.VideoCapture(input_path)
        _net = Net(model_name)

        while _video.isOpened():
            if _index >= total_frames:
                break
            ret, frame = _video.read()
            if not ret:
                break

            # 缩放到320高度
            height, width = frame.shape[0], frame.shape[1]
            ratio = width / height
            s_height = 320
            s_width = int(s_height * ratio)
            frame = cv2.resize(frame, (s_width, s_height))
            # BGR转RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results_dict[_index] = remove_many([frame], _net)[0]

            _index += 1
        else:
            error_dict["error"] = "unexpected file closure"
    except Exception as e:
        error_dict["error"] = str(e)
    finally:
        if _video:
            _video.release()
        print(f'transparent background finished: {_index}')


# 关闭进程
def _kill_proc(proc_list, output_proc):
    for proc in proc_list:
        if proc.is_alive():
            proc.kill()
    if output_proc is not None:
        output_proc.stdin.close()
        output_proc.kill()
        output_proc.wait()


# 校验异常
def _check_error(error_dict, proc_list, output_proc):
    if error_dict.get("error"):
        _kill_proc(proc_list, output_proc)
        raise ToolsRuntimeError(error_dict.get("error"))


# 校验超时
def _check_timeout(start_time, timeout, proc_list, output_proc):
    if (timeout is not None) and (time.time() - start_time > timeout):
        _kill_proc(proc_list, output_proc)
        raise ToolsTimeoutError("transparent timeout")


# 生成蒙版
def matte_key(input_path, matte_path, model_name, total_frames, frame_rate, timeout):
    manager = multiprocessing.Manager()
    results_dict = manager.dict()
    error_dict = manager.dict()

    start_time = time.time()

    worker = multiprocessing.Process(target=_deal_frames, args=(input_path, model_name, total_frames, results_dict, error_dict))
    worker.start()

    proc = None
    for i in range(total_frames):
        _check_error(error_dict, [worker], proc)
        _check_timeout(start_time, timeout, [worker], proc)
        while i not in results_dict:
            _check_error(error_dict, [worker], proc)
            _check_timeout(start_time, timeout, [worker], proc)
            time.sleep(0.1)

        frame = results_dict[i]
        del results_dict[i]

        if proc is None:
            command = ['ffmpeg', '-y', '-f', 'rawvideo', '-vcodec', 'rawvideo',
                       '-s', f"{frame.shape[1]}x{frame.shape[0]}", '-pix_fmt', 'gray',
                       '-r', f"{frame_rate}", '-i', '-',
                       '-an', '-vcodec', 'mpeg4', '-b:v', '2000k', '%s' % matte_path]
            proc = sp.Popen(command, stdin=sp.PIPE)
        proc.stdin.write(frame.tostring())

    worker.join()
    proc.stdin.close()
    proc.wait()


# 合并蒙版
def alpha_merge(input_path, matte_path, output_path, fmt):
    print('alpha merge start...')
    if fmt == 'mov':
        c_v = 'qtrle'
    elif fmt == 'webm':
        c_v = 'libvpx-vp9'
    else:
        raise ToolsValueError('output format allow only mov/webm')

    cmd = r'ffmpeg -v error -i {} -i {} ' \
          r'-filter_complex "[1][0]scale2ref[mask][main];[main][mask]alphamerge=shortest=1" ' \
          r'-c:v {} -shortest {} -y'.format(input_path, matte_path, c_v, output_path)

    process = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = process.communicate()
    if stderr:
        raise ToolsRuntimeError(stderr)
    print('alpha merge finished!')


def transparent(input_path: str, output_path: str, model_name: str, total_frames: int, frame_rate: int, timeout: int):
    # 仅允许输出mov和webm格式
    fmt = output_path.split('.')[-1].lower()
    if fmt not in ['mov', 'webm']:
        raise ToolsValueError('output format allow only mov/webm')

    temp_matte = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
    temp_matte_path = temp_matte.name.replace("\\", "/")
    temp_matte.close()

    try:
        matte_key(input_path, temp_matte_path, model_name, total_frames, frame_rate, timeout)
        alpha_merge(input_path, temp_matte_path, output_path, fmt)
    finally:
        if os.path.exists(temp_matte_path):
            os.remove(temp_matte_path)
