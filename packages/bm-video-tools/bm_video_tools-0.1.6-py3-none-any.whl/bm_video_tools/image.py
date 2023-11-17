from __future__ import annotations
import asyncio
import json
import os
import functools

from .operate import Operate
from .error import ToolsFileError

from .utils.utils import backslash2slash, get_fmt, make_output_dirs
from .utils.async_utils import async_subprocess_exec, async_pre_operate

from .remover.transparent_image import transparent
from .detection.face_detection_image import face_detection


class Image:
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

    async def run(self, op: Operate, output_path: str) -> Image:
        """
        执行操作
        :param op: Operation实例对象
        :param output_path: 输出路径
        :return: 媒体对象
        """
        output_path = backslash2slash(output_path)
        make_output_dirs(output_path)

        cmd = op.exec(o_v=True)
        await async_subprocess_exec(cmd, self.input_path, output_path)

        return self.__class__(output_path)

    @async_pre_operate
    async def remove(self, output_path: str, model_name: str = 'u2net', **kwargs) -> Image:
        """
        人像抠图
        :param output_path: 输出路径
        :param model_name: 模型名称
        :return: 图片对象
        """
        output_path = backslash2slash(output_path)
        make_output_dirs(output_path)

        temp_media: Image = kwargs.get("temp_media")
        input_path = temp_media.input_path if temp_media else self.input_path

        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, functools.partial(transparent, input_path, output_path, model_name))

        return self.__class__(output_path)

    @async_pre_operate
    async def face_detection(self, model_name: str = 'haarcascade_frontalface_alt2', **kwargs) -> bool:
        """
        检测人脸
        :param model_name: 人脸检测模型
        :return 图片中是否包含人脸
        """
        temp_media: Image = kwargs.get("temp_media")
        input_path = temp_media.input_path if temp_media else self.input_path

        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, functools.partial(face_detection, input_path, model_name))

        return result
