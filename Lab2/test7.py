import sys


def check(x):
    x = int(x)
    if (x % 100 == 0):
        if (x % 400 == 0):
            return 1
        else:
            return 0
    else:
        if (x % 4 == 0):
            return 1
        else:
            return 0
#判断是否为闰年

mth1 = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
mth2 = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
cst = input("y,m,d ")
cst = cst.split(',')
cst = list(map(int, cst))
y = cst[0]
m = cst[1]
d = cst[2]
ans = 0
if (check(y) == 0):
    for i in range(0, m - 1):
        ans = ans + mth1[i]
    if (d > mth1[m-1]):
        print('data error')
        sys.exit(0)
    ans = ans + d
else:
    for i in range(0, m - 1):
        ans = ans + mth2[i]
    if (d > mth2[m-1]):
        print('data error')
        sys.exit(0)
    ans = ans + d
print(ans)
#再根据月份进行判断再进行累加

