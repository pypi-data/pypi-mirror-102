
class resException(Exception):

    def __init__(self,res_dict):
        self.res_dict = res_dict
        self.msg = self.res_dict['Emsg'] 

    def getRes_dict(self):
        return res_dict
    
    pass

class unknownError(Exception):
    def __init__(self):
        self.msg = 'Unknown Error occured! Please try again!'

    pass

class OrderNotFound(Exception):
    
    def __init__(self,oId):
        self.oId = oId
        self.msg = self.oId+' Order info Not found!'
    pass