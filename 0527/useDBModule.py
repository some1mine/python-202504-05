from DBModule import Database

db = Database()

def output():
    sql = 'select * from tb_member'
    rows = db.executeAll(sql)
    for row in rows: print(row)
    db.close()

def exist(user_id):
    sql = "select 1 from tb_member where user_id = %s"
    result = db.executeOne(sql, (user_id))
    if result: print('이미 존재하는 아이디입니다.')
    return result

def with_id_check():
    user_id = input('아이디 : ')
    while exist(user_id): user_id = input('아이디 : ')
    password = input('패스워드 : ')
    user_name = input('이름 : ')
    email = input('이메일 : ')
    phone = input('전화 : ')
    sql = '''
        insert into tb_member(user_id, password, user_name, email, phone, regdate)
        values(%s, %s, %s, %s, %s, now())
    '''
    db.executeOne(sql, (user_id, password, user_name, email, phone))
    db.db.commit()

def member_register():
    user_id = input('아이디 : ')
    password = input('패스워드 : ')
    user_name = input('이름 : ')
    email = input('이메일 : ')
    phone = input('전화 : ')
    sql = '''
        insert into tb_member(user_id, password, user_name, email, phone, regdate)
        values(%s, %s, %s, %s, %s, now())
    '''
    db.executeOne(sql, (user_id, password, user_name, email, phone))
    db.db.commit()

if __name__ == '__main__':
    with_id_check()
    output()

