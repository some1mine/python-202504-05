print('\n\n'.join(
    ['\n'.join([
        '\t\t'.join([
            f'{(i * 3 + k)} * {j} = {(i * 3 + k) * j}' 
        for k in range(1, 4)])
    for j in range(1, 10)])
for i in range(3)]))
