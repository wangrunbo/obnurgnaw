class Error(Exception):
    """
    基础异常
    """
    message = None

    def __init__(self, message=None):
        self.message = message


class CommendError(Error):
    """
    输入命令异常
    """
    pass
