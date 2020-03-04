
class userInfo(object):
    def __init__(self):
        self.allowedUsers = {'ye':'1234','ke': '1234','justin':'1234','hayley':'1234','admin':'password'}

    def addUser(self, newID, newPwd):
        self.allowedUsers[newID] = newPwd

    def amendPassword(self,id, newPwd):
        self.allowedUsers[id] = newPwd
    
    def delUser(self, id,):
        del self.allowedUsers[id]

userInfo = userInfo()
