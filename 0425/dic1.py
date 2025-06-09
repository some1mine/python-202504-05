colors = {'red':'빨간색','blue':'파란색','green':'초록색'} #같은 키 -> 덮어씀

print(colors['red'])
print(colors['green'])
print(colors['blue'])

print(colors.keys())

colors['black'] = '검은색'
print(colors.keys())
colors['red'] = '빨강'
print(colors)

if 'pink' in colors.keys(): print(colors['pink'])
else: print('pink is not exists')

print(colors.items())
print(colors.values())

print(colors.pop('red'))
del colors['blue']
print(colors)

colors.clear()
print(colors)
