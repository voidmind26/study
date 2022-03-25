from cmath import sqrt

a = input('请输入a,b,c(以空格分隔)')
a = a.split(' ')
for i in range(len(a)):
    a[i] = float(a[i])
delta = pow(a[1], 2) - 4 * a[0] * a[2]
ans = 0
if delta == 0:
    ans = -a[1] / (2 * a[0])
    print("x1=x2=", ans)
else:
    ans = (-a[1] + sqrt(delta)) / (2 * a[0])
    ans2 = (-a[1] - sqrt(delta)) / (2 * a[0])
    print("x1=", ans, " x2=", ans2)
