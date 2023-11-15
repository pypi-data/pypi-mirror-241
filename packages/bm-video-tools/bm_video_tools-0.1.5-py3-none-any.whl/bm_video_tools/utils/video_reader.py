import os
import subprocess as sp

from moviepy.compat import DEVNULL
from moviepy.config import get_setting
from moviepy.video.io.ffmpeg_reader import FFMPEG_VideoReader
from moviepy.editor import VideoFileClip

"""
    自定义VideoReader、VideoFileClip
        增加参数：读取视频帧信息时的编码器
        webm格式视频需指定输入编码器为 libvpx-vp9，否则无法读取透明遮罩信息
"""


class VideoReader(FFMPEG_VideoReader):
    def __init__(self, filename, codec=None,
                 print_infos=False, bufsize=None,
                 pix_fmt="rgb24", check_duration=True,
                 target_resolution=None, resize_algo='bicubic',
                 fps_source='tbr'):
        self.codec = codec
        super().__init__(filename, print_infos,
                         bufsize, pix_fmt,
                         check_duration, target_resolution,
                         resize_algo, fps_source)

    def initialize(self, starttime=0):
        self.close()

        if starttime != 0:
            offset = min(1, starttime)
            i_arg = ['-ss', "%.06f" % (starttime - offset),
                     '-i', self.filename,
                     '-ss', "%.06f" % offset]
        else:
            i_arg = ['-i', self.filename]

        if self.codec:
            i_arg = ["-vcodec", self.codec, *i_arg]

        cmd = ([get_setting("FFMPEG_BINARY")] + i_arg +
               ['-loglevel', 'error',
                '-f', 'image2pipe',
                '-vf', 'scale=%d:%d' % tuple(self.size),
                '-sws_flags', self.resize_algo,
                "-pix_fmt", self.pix_fmt,
                '-vcodec', 'rawvideo', '-'])
        popen_params = {"bufsize": self.bufsize,
                        "stdout": sp.PIPE,
                        "stderr": sp.PIPE,
                        "stdin": DEVNULL}

        if os.name == "nt":
            popen_params["creationflags"] = 0x08000000

        self.proc = sp.Popen(cmd, **popen_params)


class CusVideoFileClip(VideoFileClip):
    def __init__(self, filename, codec=None,
                 has_mask=False, audio=True,
                 audio_buffersize=200000, target_resolution=None,
                 resize_algorithm='bicubic', audio_fps=44100,
                 audio_nbytes=2, verbose=False,
                 fps_source='tbr'):
        super().__init__(filename, has_mask,
                         audio, audio_buffersize,
                         target_resolution, resize_algorithm,
                         audio_fps, audio_nbytes,
                         verbose, fps_source)
        pix_fmt = "rgba" if has_mask else "rgb24"
        self.reader = VideoReader(filename, codec=codec, pix_fmt=pix_fmt,
                                  target_resolution=target_resolution,
                                  resize_algo=resize_algorithm,
                                  fps_source=fps_source)
