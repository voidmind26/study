def jc(x):
    t = 1
    for i in range(1, x):
        t = t * i
    return t
#函数用于求阶乘

p = input('Cni ')
p = p.split(' ')
p = list(map(int, p))
n = p[0]
i = p[1]
ans = jc(n) / jc(i) / jc(n - i)
ans = int(ans)
print(ans)
