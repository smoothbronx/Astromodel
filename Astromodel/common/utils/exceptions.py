class KuramotoExceptionsBase(Exception):
    def __init__(self, message: str):
        self.__message = message

    def raise_this(self):
        raise self

    def __repr__(self):
        return self.__message

class DataException(KuramotoExceptionsBase):
    def __init__(self, message: str):
        super().__init__(message)