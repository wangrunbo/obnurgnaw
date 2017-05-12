class Error(Exception):
    """
    基础异常
    """
    message = ''

    def __str__(self):
        if self.args:
            self.message = self.args[0] if len(self.args) == 1 else self.args

        return str(self.message)
