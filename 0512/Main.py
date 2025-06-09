import pickle; import sys; import os
from Board import Posts; from Member import User, Users; import Regexes
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

users = Users(); posts = Posts(); curUser : User = None

'''
회원 기능
'''

def join():
    userId = input('아이디를 입력해주세요 : ')
    while users.isDuplicated(userId): 
        print('이미 존재하는 아이디입니다.')
        userId = input('아이디를 입력해주세요 : ')
    password = input('비밀번호를 입력해주세요 : ')
    name = input('이름을 입력해주세요 : ')
    phone = input('전화번호를 입력해주세요 : ')
    while not Regexes.phoneForm(phone):
        print('전화번호 형식을 맞춰주세요.')
        phone = input('전화번호를 입력해주세요 : ')
    email = input('이메일을 입력해주세요 : ')
    while not Regexes.emailForm(email):
        print('이메일 형식을 맞춰주세요.')
        email = input('이메일을 입력해주세요 : ')
    users.join(User(userId, password, name, phone, email, users.idx))
    print('가입했습니다.')

def leave():
    global curUser
    if curUser is not None:
        users.leave(curUser); curUser = None
        print('탈퇴했습니다.')

def login():
    global curUser
    userId = input('아이디 : ')
    password = input('비밀번호 : ')
    for u in users.table.values():
        if u.userId == userId and u.password == password: 
            curUser = u; print('로그인했습니다.'); return
    print('일치하는 회원 정보가 없습니다.')

def logout():
    global curUser
    curUser = None
    print('로그아웃했습니다.')

def myInfo():
    if curUser is not None: print(curUser)    
    
def updateMyInfo():
    global curUser
    password = input('비밀번호를 입력해주세요 : ')
    name = input('이름을 입력해주세요 : ')
    phone = input('전화번호를 입력해주세요 : ')
    while not Regexes.phoneForm(phone):
        print('전화번호 형식을 맞춰주세요.')
        phone = input('전화번호를 입력해주세요 : ')
    email = input('이메일을 입력해주세요 : ')
    while not Regexes.emailForm(email):
        print('이메일 형식을 맞춰주세요.')
        email = input('이메일을 입력해주세요 : ')
    curUser.modify(password, name, phone, email)
    print('회원님의 정보를 수정했습니다.')

'''
게시판 기능
'''

def boardList():
    posts.list()

def myList():
    print('나의 작성 게시글')
    posts.myList(curUser)

def write():
    title = input('제목을 입력해주세요 : ')
    content = input('내용을 입력해주세요 : ')
    posts.write(curUser, title, content)

def update():
    try:
        myList()
        targetIdx = int(input('수정할 글 번호를 입력해주세요 : '))
        title = input('제목을 입력해주세요 : ')
        content = input('내용을 입력해주세요 : ')
        posts.modify(targetIdx, curUser, title, content)
    except ValueError as e: print('숫자로 입력해주세요')

def delete():
    try:
        myList()
        targetIdx = int(input('삭제할 글 번호를 입력해주세요 : '))
        posts.delete(targetIdx, curUser)
    except ValueError as e: print('숫자로 입력해주세요.')

'''
저장 관련 기능(직렬화/역직렬화)
'''

def save():
    os.makedirs('data', exist_ok = True)
    with open('data/board.tmp', 'wb') as file: pickle.dump(posts, file)
    with open('data/member.tmp', 'wb') as file: pickle.dump(users, file)

def load():
    global users, posts
    try:
        with open('data/board.tmp', 'rb') as file: posts = pickle.load(file)
        with open('data/member.tmp', 'rb') as file: users = pickle.load(file)
    except (FileNotFoundError, EOFError, pickle.UnpicklingError) as e: return

nonLoginFuncs = {'1' :join, '2' : login, '3' : boardList, '4' : write}
loginFuncs = {'1' : logout, '2' : leave, '3' : myInfo, '4' : updateMyInfo, '5' : myList, '6' : boardList, '7' : write, '8' : update, '9' : delete}

def main():
    print('====== 게시판 ======')
    while True:
        load()
        print('메뉴를 숫자로 골라주세요')
        if curUser is None: 
            choice = input('1.회원가입 | 2.로그인 | 3.글 목록 | 4.글 작성 | 0.종료 : ').strip()
            if choice == '0': return
            elif choice in nonLoginFuncs.keys(): nonLoginFuncs[choice]()
            else: print('잘못된 입력입니다.')
        else: 
            choice = input('1.로그아웃 | 2.회원탈퇴 | 3.내 정보 보기 | 4.내 정보 수정 | 5.내 작성글 목록 보기 | 6.전체 글 목록 | 7.글 작성 | 8.글 수정 | 9.글 삭제 | 0.종료 : ').strip()
            if choice == '0': return
            elif choice in loginFuncs.keys(): loginFuncs[choice]()
            else: print('잘못된 입력입니다.')
        save()
        
if __name__ == '__main__': 
    main()