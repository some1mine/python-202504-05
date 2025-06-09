import sys; import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

result = {}; features = []
with open('data/iris.csv', 'r') as file:
    features = file.readline().rstrip().split(',')
    data = [*map(lambda x: x.rstrip().split(','), file.readlines())]
    for s in set(map(lambda x: x[-1], data)): result[s] = {'sepal' : [], 'petal' : []}
    for d in data:
        lst = list(map(float, d[:-1]))
        result[d[-1]]['sepal'].append(lst[:2])
        result[d[-1]]['petal'].append(lst[2:])

for k in result.keys(): 
    print(k)
    print(f"\n======================== {k} sepal =======================\n")
    for d in result[k]['sepal']:
        print(f"{k} \
              sepal : length = \t \
              {d[0]:20}, \
                    width = {d[1]:20}")
    print(f"{k} \
          avg sepal : length = \t \
          {sum([*map(lambda x : x[0], result[k]['sepal'])]) / len(result[k]['sepal']):20}, \
                width = {sum([*map(lambda x : x[1], result[k]['sepal'])]) / len(result[k]['sepal']):20}")
    
    print(f"\n======================== {k} petal =======================\n")
    for d in result[k]['petal']:
        print(f"{k} \
              petal : length = \t \
              {d[0]:20}, \
                    width = {d[1]:20}")
    print(f"{k} \
          avg petal : length = \t \
          {sum([*map(lambda x : x[0], result[k]['petal'])]) / len(result[k]['petal']):20}, \
                width = {sum([*map(lambda x : x[1], result[k]['petal'])]) / len(result[k]['petal']):20}")
    print()