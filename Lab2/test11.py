l1 = input('')
l1 = l1.split(' ')
l2 = set(l1)
l2 = list(l2)
l2.sort(key=l1.index)
for i in range(len(l2)):
    print(l2[i], end=' ')
#通过set去重，再规定键值排序