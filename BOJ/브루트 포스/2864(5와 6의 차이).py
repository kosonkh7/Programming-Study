a, b = map(list, input().split())

amax = ''
amin = ''
bmax = ''
bmin = ''

for i in a:
    if i == '5':
        amax = amax + '6'
        amin = amin + '5'
    elif i == '6':
        amax = amax + '6'
        amin = amin + '5'
    else:
        amax = amax + i
        amin = amin + i
    
for i in b:
    if i == '5':
        bmax = bmax + '6'
        bmin = bmin + '5'
    elif i == '6':
        bmax = bmax + '6'
        bmin = bmin + '5'
    else:
        bmax = bmax + i
        bmin = bmin + i

print(int(amin)+int(bmin), int(amax)+int(bmax))