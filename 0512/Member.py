class User:
    def __init__(self, userId : str, password : str, name : str, phone : str, email : str, userNo : int = -1):
        self.userId = userId
        self.password = password
        self.name = name
        self.phone = phone
        self.email = email
        self.userNo = userNo
            
    def __str__(self):
        return f'회원번호 {self.userNo} 아이디 {self.userId} 이름 {self.name} 전화번호 {self.phone} 이메일 {self.email}'

    def modify(self, password : str, name : str, phone : str, email : str):
        self.password = password
        self.name = name
        self.phone = phone
        self.email = email

class Users:
    def __init__(self):
        self.table : dict[int, User] = {}
        self.idSet : set[str] = set()
        self.idx = 0

    def join(self, user : User):
        self.table[self.idx] = user
        self.idSet.add(user.userId)
        self.idx += 1

    def isDuplicated(self, userId):
        return userId in self.idSet
    
    def leave(self, user : User):
        self.idSet.discard(user.userId)
        del self.table[user.userNo]