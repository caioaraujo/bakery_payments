class LargeNameException(Exception):
    def __init__(self, message=None, errors=None):
        super(LargeNameException, self).__init__(message)
        self.errors = errors