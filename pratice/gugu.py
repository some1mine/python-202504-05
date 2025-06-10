for i in range(3):
    for j in range(1, 10):
        print('\t\t'.join([f'{(i * 3 + k)} * {j} = {(i * 3 + k) * j}' for k in range(1, 4)]))
    print()