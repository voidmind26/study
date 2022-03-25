from cmath import sqrt

a = input('请输入一个数')
a = int(a)
if (a < 2):
    print('no')
else:
    for i in range(2, int(sqrt(a).real) + 1):
        if a % i == 0:
            print('no')
            break
        else:
            print('yes')
            break
