from __future__ import annotations
import asyncio
import json
import os
import functools
import math
from moviepy.editor import concatenate_videoclips, CompositeVideoClip, ImageClip, AudioFileClip

from .operate import Operate
from .image import Image
from .audio import Audio
from .error import ToolsFileError

from .utils.utils import backslash2slash, get_fmt, make_output_dirs
from .utils.async_utils import async_subprocess_exec, async_pre_operate, async_pre_operate_batch
from .utils.video_reader import CusVideoFileClip

from .remover.transparent_video import transparent
from .detection.face_detection_video import face_detection


class Video:
    def __init__(self, input_path: str):
        self.input_path = backslash2slash(input_path)
        self.fmt = get_fmt(self.input_path)

        if not os.path.exists(self.input_path):
            raise ToolsFileError(f"{self.input_path} does not exist")

    async def get_info(self) -> dict:
        """
        查看媒体信息
        :return: 媒体详细信息
        """
        cmd = r'ffprobe -i {} -v error -show_format -show_streams -print_format json'
        res = await async_subprocess_exec(cmd, self.input_path)
        return json.loads(res)

    async def run(self, op: Operate, output_path: str) -> Video:
        """
        执行操作
        :param op: Operation实例对象
        :param output_path: 输出路径
        :return: 媒体对象
        """
        output_path = backslash2slash(output_path)
        make_output_dirs(output_path)

        if self.fmt == "webm":
            cmd = op.exec(input_params={
                "-c:v": "libvpx-vp9"
            })
        else:
            cmd = op.exec()

        await async_subprocess_exec(cmd, self.input_path, output_path)

        return self.__class__(output_path)

    @async_pre_operate
    async def screenshot(self, output_path: str, **kwargs) -> Image:
        """
        视频截图
        :param output_path: 输出图片存放路径
        :return: 图片对象
        """
        output_path = backslash2slash(output_path)
        make_output_dirs(output_path)

        temp_media: Video = kwargs.get("temp_media")
        input_path = temp_media.input_path if temp_media else self.input_path

        cmd = r'ffmpeg -i {} -ss 0 -frames:v 1 -y -v error {}'
        await async_subprocess_exec(cmd, input_path, output_path)

        return Image(output_path)

    @async_pre_operate
    async def remove(self, output_path: str,
                     model_name: str = 'u2net',
                     frame_limit: int = -1, frame_rate: int = -1,
                     timeout: int = None, **kwargs) -> Video:
        """
        人像抠图
        :param output_path: 输出路径
        :param model_name: 模型名称
        :param frame_limit: 总帧数
        :param frame_rate: 帧率
        :param timeout: 超时时间（秒）
        :return: 视频对象
        """
        output_path = backslash2slash(output_path)
        make_output_dirs(output_path)

        temp_media: Video = kwargs.get("temp_media")

        if temp_media:
            input_path = temp_media.input_path
            video_info = await temp_media.get_info()
        else:
            input_path = self.input_path
            video_info = await self.get_info()

        video_stream = next((s for s in video_info["streams"] if s["codec_type"] == "video"), None)
        if not video_stream:
            raise ToolsFileError("no video stream")

        total_frames = int(video_stream["nb_frames"])
        if frame_limit != -1:
            total_frames = min(frame_limit, total_frames)

        fr = video_stream["r_frame_rate"]
        if frame_rate == -1:
            print(F"FRAME RATE DETECTED: {fr} (if this looks wrong, override the frame rate)")
            frame_rate = math.ceil(eval(fr))

        print(F"FRAME RATE: {frame_rate} TOTAL FRAMES: {total_frames}")

        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, functools.partial(transparent, input_path, output_path, model_name, total_frames, frame_rate, timeout))

        return self.__class__(output_path)

    @async_pre_operate
    async def face_detection(self, model_name: str = 'haarcascade_frontalface_alt2', proportion: float = 0.9, timeout: int = None, **kwargs) -> bool:
        """
        视频逐帧检测人脸
        :param model_name: 人脸检测模型
        :param proportion: 人脸出现占比（0~1）
        :param timeout: 超时时间（秒）
        :return 视频中人脸占比是否超过指定值
        """
        temp_media: Video = kwargs.get("temp_media")
        input_path = temp_media.input_path if temp_media else self.input_path

        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, functools.partial(face_detection, input_path, model_name, proportion, timeout))

        return result

    @staticmethod
    @async_pre_operate_batch(("Video",))
    async def concat(output_path: str, video_list: list, audio: Audio = None, logger: bool = False) -> Video:
        """
        视频拼接
        :param output_path: 输出视频路径
        :param video_list: 视频列表
        :param audio: 音频
        :param logger: 是否打印进度
        :return: 视频对象
        """
        output_path = backslash2slash(output_path)
        make_output_dirs(output_path)

        def _content():
            clips = []
            audio_clip = None
            final_clip = None

            try:
                for item in video_list:
                    media = item["media"]

                    if media.fmt == 'webm':
                        clip = CusVideoFileClip(media.input_path, codec="libvpx-vp9", has_mask=True)
                    elif media.fmt == 'mov':
                        clip = CusVideoFileClip(media.input_path, has_mask=True)
                    else:
                        clip = CusVideoFileClip(media.input_path)

                    clips.append(clip)

                final_clip = concatenate_videoclips(clips, method="compose")

                # 修改音频
                if audio:
                    audio_clip = AudioFileClip(audio.input_path)
                    final_clip = final_clip.set_audio(audio_clip)

                # 保存文件
                output_fmt = get_fmt(output_path)
                if output_fmt == 'webm':
                    final_clip.write_videofile(output_path, codec="libvpx-vp9", logger='bar' if logger else None)
                else:
                    final_clip.write_videofile(output_path, logger='bar' if logger else None)
            finally:
                for video_clip in clips:
                    video_clip.close()
                if audio_clip:
                    audio_clip.close()
                if final_clip:
                    final_clip.close()

        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, _content)

        return Video(output_path)

    @staticmethod
    @async_pre_operate_batch(("Video", "Image"))
    async def composite(output_path: str, media_list: list, audio: Audio = None, canvas: tuple = None, logger: bool = False):
        """
        视频合成
        :param output_path: 输出路径
        :param media_list: 视频列表
        :param audio: 音频
        :param canvas: 画布大小
        :param logger: 是否打印进度
        :return: 视频对象
        """
        output_path = backslash2slash(output_path)
        make_output_dirs(output_path)

        def _composite():
            clips = []
            audio_clip = None
            final_clip = None
            try:
                for item in media_list:
                    media = item["media"]

                    if isinstance(media, Image):
                        clip_class = ImageClip
                        if ("end" not in item) and ("duration" not in item):
                            item["duration"] = 10
                    else:
                        clip_class = CusVideoFileClip

                    if media.fmt == 'webm':
                        clip = clip_class(media.input_path, codec="libvpx-vp9", has_mask=True)
                    elif media.fmt == 'mov':
                        clip = clip_class(media.input_path, has_mask=True)
                    else:
                        clip = clip_class(media.input_path)

                    clip_audio = clip.audio
                    clip = clip.without_audio()

                    if "x" in item or "y" in item:
                        x, y = item.get("x", 0), item.get("y", 0)
                        clip = clip.set_position((x, y))

                    if "start" in item:
                        start = item.get("start")
                        clip = clip.set_start(start)
                        if clip_audio:
                            clip_audio = clip_audio.set_start(start)

                    if "end" in item:
                        end = item.get("end")
                        clip = clip.set_end(end)
                        if clip_audio and end < clip_audio.end:
                            clip_audio = clip_audio.set_end(end)
                    elif "duration" in item:
                        duration = item.get("duration")
                        clip = clip.set_duration(duration)
                        if clip_audio and duration < clip_audio.duration:
                            clip_audio = clip_audio.set_duration(duration)

                    if clip_audio:
                        clip = clip.set_audio(clip_audio)
                    clips.append(clip)

                # 修改画布大小
                if canvas:
                    final_clip = CompositeVideoClip(clips, size=canvas)
                else:
                    final_clip = CompositeVideoClip(clips)

                # 修改音频
                if audio:
                    audio_clip = AudioFileClip(audio.input_path)
                    final_clip = final_clip.set_audio(audio_clip)

                # 保存文件
                output_fmt = get_fmt(output_path)
                if output_fmt == 'webm':
                    final_clip.write_videofile(output_path, codec="libvpx-vp9", fps=25, logger='bar' if logger else None)
                else:
                    final_clip.write_videofile(output_path, fps=25, logger='bar' if logger else None)
            finally:
                # 释放资源
                for video_clip in clips:
                    video_clip.close()
                if audio_clip:
                    audio_clip.close()
                if final_clip:
                    final_clip.close()

        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, _composite)

        return Video(output_path)
