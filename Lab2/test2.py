a = eval(input('请输入一个正整数'))
s = []
a = int(a)
ln = 0
while a != 0:
    ln = ln + 1
    s.append(a % 10)
    a = a / 10
    a = int(a)
print("这个数的长度是", ln, ",逆序输出结果是", s)

#取模取出一位数再通过整除将其删去
#从而得到每一位数和位数