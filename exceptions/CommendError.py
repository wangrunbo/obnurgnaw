from exceptions import Error


class CommendError(Error):
    """输入命令异常"""
    message = '指令未识别！'


class AttributeNotFoundError(CommendError):
    """类属性未定义"""
    pass


class ObjectNotExistError(CommendError):
    """对象不存在"""
    pass
