lst = [1, 2, 3]
for i in range(3, 15):
    lst.append(lst[i - 1] + lst[i - 2] + lst[i - 3])
print(lst[14])
