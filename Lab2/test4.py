a = [1, 1, 2, 3]
x = int(input("请输入项数 "))
for i in range(0, x):
    if (i < len(a)):
        continue
    a.append(a[i - 1] + a[i-2])
print(a[x - 1])
#通过递推求斐波那契数列