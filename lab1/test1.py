x = input('输入三位数')
x = int(x)
print('三位数分别为')
for i in range(1, 4):
    a = x % 10
    a = int(a)
    x = x / 10
    print(a)
