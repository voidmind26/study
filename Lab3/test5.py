from cmath import sqrt


def judge(a):
    sq = sqrt(a).real
    sq = int(sq)
    if a <= 1:
        return 0
    for i in range(2, sq):
        if a % i == 0:
            return 0
    return 1


a = input('input a num ')
a = int(a)
f = judge(a)
if f == 1:
    print("yes")
else:
    print("no")
