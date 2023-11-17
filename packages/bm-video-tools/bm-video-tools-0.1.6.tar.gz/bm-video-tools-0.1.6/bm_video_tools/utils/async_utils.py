import asyncio
import shlex
import tempfile
import os

from .utils import backslash2slash
from ..operate import Operate
from ..error import ToolsRuntimeError, ToolsValueError


async def async_subprocess_exec(cmd: str, *args) -> bytes:
    cmd = cmd.format(*args)
    print(f'exec: {cmd}')
    proc = await asyncio.create_subprocess_exec(*shlex.split(cmd), stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    if stderr:
        raise ToolsRuntimeError(stderr.decode('utf-8'))
    return stdout


def async_pre_operate(func):
    async def inner(self, *args, **kwargs):
        if "op" in kwargs and isinstance(kwargs.get("op"), Operate):
            op = kwargs.get("op")

            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=f'.{self.fmt}')
            temp_file_path = backslash2slash(temp_file.name)
            temp_file.close()
            try:
                temp_media = await self.run(op, temp_file_path)
                result = await func(self, *args, **kwargs, temp_media=temp_media)
                return result
            finally:
                if os.path.exists(temp_file_path):
                    os.remove(temp_file_path)
        else:
            result = await func(self, *args, **kwargs)
            return result

    return inner


def async_pre_operate_batch(allowable):
    def wrapper(func):
        async def inner(output_path, media_list, *args, **kwargs):
            temp_path_list = []
            try:
                new_media_list = []
                for item in media_list:
                    media = item["media"]
                    if type(media).__name__ not in allowable:
                        raise ToolsValueError(f"the {type(media).__name__} object cannot be accepted")

                    if "op" in item and isinstance(item.get("op"), Operate):
                        op = item.get("op")
                        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=f'.{media.fmt}')
                        temp_file_path = backslash2slash(temp_file.name)
                        temp_file.close()

                        temp_path_list.append(temp_file_path)
                        media = await media.run(op, temp_file_path)

                    new_media_list.append({
                        **item,
                        "media": media,
                    })
                result = await func(output_path, new_media_list, *args, **kwargs)
                return result
            finally:
                for temp_path in temp_path_list:
                    if os.path.exists(temp_path):
                        os.remove(temp_path)

        return inner

    return wrapper
