from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine(
    'mysql+pymysql://root:1234@localhost/mydb',
    pool_size = 10,
    max_overflow = 5,
    pool_recycle = 3600
)

try:
    conn = engine.connect()

    sql = text('select * from emp')
    rows = conn.execute(sql)
    for row in rows: print(row)

    rows = rows.mappings().all()
    for row in rows: print(row)

    sql = text('''
        insert into emp(empno, ename, sal) values(:empno, :ename, :sal)
    ''')

    conn.execute(sql, [{'empno' : 10000, 'ename' : '우즈', 'sal' : 8000}])

    conn.commit()
    conn.close()
    print('성공')
    
except SQLAlchemyError as e:
    print('실패', e)
finally:
    if conn: conn.close()
    print('종료')