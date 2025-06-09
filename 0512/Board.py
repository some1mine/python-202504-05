import time; from Member import User

class Post:
    def __init__(self, user : User, title : str, content : str, idx : int = -1):
        self.idx = idx
        self.user = user
        self.title = title
        self.content = content
        self.madeTime = time.time()
        self.updateTime = None
        self.hitCnt = 0

    def upCnt(self):
        self.hitCnt += 1

    def modify(self, title : str, content : str):
        self.title = title
        self.content = content
        self.updateTime = time.time()

    def output(self):
        print(self.idx, end = '\t')
        print(self.title, '\n')
        print(self.content, '\n')
        print('작성시간 ', self.madeTime, end = '\t')
        if self.updateTime : print('수정시간 ', self.updateTime)
        print(self.hitCnt, '\n')
        print(('작성자 ', self.user.userId, self.user.name) if self.user is not None else '익명')

class Posts:
    def __init__(self):
        self.table : dict[int, Post] = {}; self.idx = 0
        
    def list(self):
        for b in self.table.values(): b.output()
    
    def myList(self, user : User):
        for b in self.table.values():
            if b.user == user: b.output()
    
    def write(self, user : User, title : str, content : str):
        self.table[self.idx] = Post(user, title, content, self.idx)
        print('작성했습니다.'); self.idx += 1

    def modify(self, targetIdx : int, user : User, title : str, content : str):
        target = self.table.get(targetIdx)
        if target is None: print(f'{targetIdx}게시글이 없습니다.')
        elif target.user == user:
            self.table[targetIdx].modify(title, content)
            print('수정했습니다.')
        else: print('로그인된 계정으로 작성한 게시물만 수정할 수 있습니다.')

    def delete(self, targetIdx : int, user : User):
        target = self.table.get(targetIdx)
        if target is None: print(f'{targetIdx}게시글이 없습니다.')
        elif target.user == user:
            del self.table[targetIdx]
            print('삭제했습니다.')
        else: print('로그인된 계정으로 작성한 게시물만 삭제할 수 있습니다.')