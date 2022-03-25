tmp = (1, 2, 3, 4)
for i in range(len(tmp)):
    for j in range(len(tmp)):
        for z in range(len(tmp)):
            if (i != j) and (j != z) and (i != z):
                print(tmp[i], tmp[j], tmp[z])
#遍历所有情况