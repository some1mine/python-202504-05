import sys; import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

dataList = []; features = []

with open('data/mpg.csv') as file :
    features = file.readline().split(',')
    for line in file.readlines(): 
        dataList.append(line.rstrip().split(','))

for s in sorted(set([d[1] for d in dataList])) :
    print(s, '::', len([*filter(lambda d : d[1] == s, dataList)]))

print(features)