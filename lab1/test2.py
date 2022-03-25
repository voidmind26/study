from cmath import pi, sqrt
from math import cos

a = input('请输入边长1 ')
b = input('请输入边长2 ')
c = input('请输入夹角')
a = float(a)
b = float(b)
c = float(c)
c = c * pi / 180
ans = a * a + b * b - 2 * cos(c) * a * b
ans = sqrt(ans).real
print('第三边长为', round(ans, 5))
