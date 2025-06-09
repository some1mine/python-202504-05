# 입출력과 저장 구조의 기본은 파일 시스템
# 파일 간의 연계 또는 연결이 필요
# 파일을 읽고 쓰는 방법은 크게 두 가지

# 파일을 열고 닫는 방법 
''' 1. open(경로를 포함한 파일명[경로 생략시 현재 폴더 기준, 없으면 만듦], 작업 유형[read, write, append])
        rsring 제외 \는 \\로
    2. with 구문을 사용하여 파일을 열고 닫는 방법
        with open('dataFile.txt', 'w') as file:              '''

# 파일을 읽는 함수는 read(한번에 다 읽음), readline(한줄씩 읽음), readlines(모든 줄을 리스트로 읽음)
# 파일을 쓰는 함수는 write(한번에 다 씀), writelines(리스트를 한꺼번에 씀)
# 파일을 닫는 함수는 close(파일을 닫음)
# 파일을 열고 닫는 것은 반드시 해야함

# 리눅스 경로 : 구분자 / | 이름에 공백 X, 확장자 구분 X, 대소문자 구분 O
# 윈도우 경로 : 구분자 \ | 이름에 공백 O, 확장자 구분 O, 대소문자 구분 X(프로그래밍 언어 또는 프로그램 환경에 따라 다름 - 경우에 따라 변환 후 재변환이 필요)

# 루트로부터 시작하는 절대경로와 현재 폴더를 기준으로 하는 상대경로
# 절대경로는 /home/user/file.txt, 상대경로는 ./file.txt(.은 현재 폴더 ..는 상위 폴더)    

with open('file/dataFile1.txt', 'w') as file:
        print('Hello World', file = file)

with open('file/dataFile2.txt', 'w') as file:
        for i in range(1, 11): file.writelines(f'i = {i}')

with open('C:/Users/user/jupyter_workspace/python_workspace1/file/dataFile3.txt', 'w') as file:
        file.writelines(list(map(lambda x : f'tmp {x}\n', range(1, 11))))