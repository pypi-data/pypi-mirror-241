class IRNException(Exception):
    msg: str

    def __init__(self, msg):
        self.msg = msg
