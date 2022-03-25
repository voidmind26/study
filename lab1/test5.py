a = input('输入两个数字')
a = a.split(' ')
for i in range(len(a)):
    a[i] = float(a[i])
ans = a[0] + a[1]
print(round(ans, 4))
