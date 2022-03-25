import sys


def check(a):
    a = str(a)
    sp = (',', '.', '?', '!', '<', '>')
    if sp.count(a) != 0:
        return 4
    elif a >= 'a' and a <= 'z':
        return 3
    elif a >= '0' and a <= '9':
        return 2
    elif a >= 'A' and a <= 'Z':
        return 1
    else:
        return -1


st = input('input password ')
le = len(st)
if le < 6:
    print('week')
    sys.exit(0)
lst = []
for i in range(len(st)):
    tmp = check(st[i])
    if (tmp == -1):
        print('input error')
        sys.exit(0)
    lst.append(tmp)
f = set(lst)
k = {1: 'week', 2: 'below middle', 3: 'above middle', 4: 'strong'}
print(k[len(f)])
