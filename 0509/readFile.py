# 파일이 존재하지 않으면 에러발생
# open('file/dataFile.txt', 'r')하고 read() 후에 read를 또 하면 데이터를 못찾음 - 파일 포인터가 맨 뒤에 가있음
# 파일 포인터를 처음으로 돌려야함 - seek(0)
# with open('file/dataFile3.txt', 'r') as file:
#     print(file.read())

# with open('file/dataFile3.txt', 'r') as file:
#     print(file.readlines())

f = open('file/dataFile3.txt', 'r')
print(f.read())
f.seek(0)

f = open('file/dataFile3.txt', 'r')
d = f.readline()
print(type(d))
print(d)
f.close()

f = open('file/dataFile3.txt', 'r')
line = f.readline()
while line: 
    print(line)
    line = f.readline()
f.close()

with open('file/dataFile3.txt', 'r') as file:
    d = file.readlines()
    print(type(d))
    print(d)