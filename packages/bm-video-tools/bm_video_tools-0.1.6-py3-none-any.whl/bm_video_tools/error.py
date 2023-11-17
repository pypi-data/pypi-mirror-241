class ToolsRuntimeError(RuntimeError):
    """
    运行异常
        - ffmpeg运行异常
    """
    pass


class ToolsTimeoutError(TimeoutError):
    """
    超时
        - 运行时长超过指定时长
    """
    pass


class ToolsFileError(Exception):
    """
    文件异常
        - 文件打开异常
        - 模型不存在
        - 地址不存在
    """
    pass


class ToolsValueError(ValueError):
    """
    值异常
        - 倍速只能在0.5~2之间
        - 媒体类型不被允许
        - 蒙版格式只能是mov、webm
        - 模型名错误
    """
    pass
