import sys

m = 1e9 + 7
m = int(m)
n = input('')
n = eval(n)
if n == 1:
    print('10\n')
    sys.exit(0)
if n == 2:
    print('9\n')
    sys.exit(0)
else:
    s = "9"
    s2 = "1"
    for i in range(1, n - 1):
        s = s2 + s
    s = eval(s)
    s = s % m
    s = int(s)
    print(s)
