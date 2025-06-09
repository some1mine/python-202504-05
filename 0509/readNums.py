d = []
with open('file/정수.txt', 'r') as file:
    d = [*map(int, filter(lambda x: x.rstrip(), file.readlines()))]
    print(sum(d) / len(d))
print(d)