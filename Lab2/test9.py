from random import randint

a = []
for i in range(1, 50):
    a.append(randint(1, 1000))
i = 0
while i < len(a):
    if a[i] % 2 == 0:
        del (a[i])
    else:
        i = i + 1
print(a)
#遍历所有元素，进行删除