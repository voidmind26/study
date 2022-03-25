lst = [1, 10, 30, 40, 60, 100, 200, 900]
x = eval(input("请输入要插入的数字 "))
res = 0
for i in range(len(lst)):
    if (x <= lst[i]):
        lst.insert(i , int(x))
        res = i
        break
print("插入位置为", res+1, "，插入后数组值为", lst)

#通过insert插入元素