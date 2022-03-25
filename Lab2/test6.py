cst = 100
ans = 0
cst = int(cst)
for i in range(1, 100):
    for j in range(0, 34):
        for k in range(0, 20):
            if (i + 3 * j + 5 * k) == 100:
                ans = ans + 1
print(ans)

#通过枚举遍历每一种情况
