def check(a):
    digit = 0
    alpha = 0
    upper = 0
    other = 0
    for i in range(len(a)):
        f = ident(a[i])
        if f == 1:
            digit = digit + 1
        elif f == 2:
            alpha = alpha + 1
        elif f == 3:
            upper = upper + 1
        elif f == 4:
            other = other + 1
    return (digit, alpha, upper, other)


def ident(a):
    a = str(a)
    if '0' <= a <= '9':
        return 1
    if 'a' <= a <= 'z':
        return 2
    if 'A' <= a <= 'Z':
        return 3
    return 4


a = input('input a string ')
ans = check(a)
print('(digit,alpha,upper,other)')
print(ans)
