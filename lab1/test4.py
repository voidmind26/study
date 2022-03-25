a = input('请输入第一个点(以逗号分隔)')
b = input('请输入第二个点(以逗号分隔)')
a = a.split(",")
a = list(map(int, a))
b = b.split(",")
b = list(map(int, b))
ans = 0
for i in range(len(a)):
    ans = ans + abs(a[i] - b[i])
print(ans)
