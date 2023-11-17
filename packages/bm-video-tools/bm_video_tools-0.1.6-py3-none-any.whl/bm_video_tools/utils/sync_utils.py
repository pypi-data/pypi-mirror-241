import subprocess
import shlex
import tempfile
import os

from .utils import backslash2slash
from ..operate import Operate
from ..error import ToolsRuntimeError, ToolsValueError


def subprocess_exec(cmd: str, *args) -> bytes:
    cmd = cmd.format(*args)
    print(f'exec: {cmd}')
    result = subprocess.run(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        raise ToolsRuntimeError(result.stderr.decode('utf-8'))
    return result.stdout


def pre_operate(func):
    def inner(self, *args, **kwargs):
        if "op" in kwargs and isinstance(kwargs.get("op"), Operate):
            op = kwargs.get("op")

            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=f'.{self.fmt}')
            temp_file_path = backslash2slash(temp_file.name)
            temp_file.close()
            try:
                temp_media = self.run(op, temp_file_path)
                result = func(self, *args, **kwargs, temp_media=temp_media)
                return result
            finally:
                if os.path.exists(temp_file_path):
                    os.remove(temp_file_path)
        else:
            result = func(self, *args, **kwargs)
            return result

    return inner


def pre_operate_batch(allowable):
    def wrapper(func):
        def inner(output_path, media_list, *args, **kwargs):
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
                        media = media.run(op, temp_file_path)

                    new_media_list.append({
                        **item,
                        "media": media,
                    })
                result = func(output_path, new_media_list, *args, **kwargs)
                return result
            finally:
                for temp_path in temp_path_list:
                    if os.path.exists(temp_path):
                        os.remove(temp_path)

        return inner

    return wrapper
