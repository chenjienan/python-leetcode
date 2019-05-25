class Request:
    def __init__(self,l = 0):
        self.level = l
        
    def getLevel(self):
        return self.level


class ExternalRequest(Request):
    def __init__(self,l = 0,d = None):
        Request.__init__(self,l)
        self.direction = d

    def getDirection(self):
        return self.direction


class InternalRequest(Request):
    def __init__(self,l = None):
        Request.__init__(self,l)