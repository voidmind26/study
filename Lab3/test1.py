from cmath import pi


def solve(a):
    return a * a * pi


r = input('please input the r ')
r = eval(r)
ans = solve(r)
print(round(ans, 3))
