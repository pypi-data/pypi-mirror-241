class LxmPayError(Exception):
    def __init__(self, errcode, errmsg, request=None, response=None):
        self.errcode = errcode
        self.errmsg = errmsg
        self.request = request
        self.response = response


class PayError(LxmPayError):
    pass
