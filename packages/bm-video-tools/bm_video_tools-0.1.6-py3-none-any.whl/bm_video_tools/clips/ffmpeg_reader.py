import os
import shlex
import json
import subprocess as sp


def ffmpeg_parse_infos(filename, print_infos=False, check_duration=True, fps_source='tbr'):
    popen_params = {"stdout": sp.PIPE,
                    "stderr": sp.PIPE}
    if os.name == "nt":
        popen_params["creationflags"] = 0x08000000

    cmd = fr"ffprobe -i {filename} -v error -show_format -show_streams -print_format json"

    result = sp.run(shlex.split(cmd), **popen_params)
    if result.returncode != 0:
        raise IOError(result.stderr.decode('utf-8'))

    infos = json.loads(result.stdout)
    if print_infos:
        print(infos)

    result = dict()
    result['duration'] = None

    if check_duration:
        try:
            result['duration'] = float(infos["format"]["duration"])
        except Exception:
            raise IOError(fr"failed to read the duration of file {filename}")

    video_stream = next((s for s in infos["streams"] if s["codec_type"] == "video"), None)
    audio_stream = next((s for s in infos["streams"] if s["codec_type"] == "audio"), None)

    result['video_found'] = (video_stream is not None)

    if result['video_found']:
        s = [video_stream.get("width"), video_stream.get("height")]
        result['video_size'] = s

        def get_tbr():
            return float(eval(video_stream["r_frame_rate"]))

        def get_fps():
            return float(eval(video_stream["avg_frame_rate"]))

        if fps_source == 'tbr':
            try:
                result['video_fps'] = get_tbr()
            except Exception as e:
                result['video_fps'] = get_fps()
        elif fps_source == 'fps':
            try:
                result['video_fps'] = get_fps()
            except Exception as e:
                result['video_fps'] = get_tbr()

        if check_duration:
            try:
                result['video_duration'] = float(video_stream['duration'])
            except Exception as e:
                result['video_duration'] = result["duration"]
            try:
                result['video_nframes'] = int(video_stream['nb_frames'])
            except Exception as e:
                result['video_nframes'] = int(result['video_duration'] * result['video_fps']) + 1
        else:
            result['video_nframes'] = 1
            result['video_duration'] = None

        result['video_rotation'] = 0

    result['audio_found'] = (audio_stream is not None)

    if result['audio_found']:
        try:
            result['audio_fps'] = int(audio_stream["sample_rate"])
        except Exception as e:
            result['audio_fps'] = 'unknown'

        try:
            result['audio_duration'] = float(audio_stream['duration'])
        except Exception as e:
            result['audio_duration'] = None

    return result
