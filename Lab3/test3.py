class mset:
    lst = []
    num = 0

    def __init__(self) -> None:  # 初始化
        self.lst = []
        self.num = 0
        pass

    def insert(self, a):  # 插入元素
        t = self.lst.count(a)
        if t == 0:
            self.lst.append(a)
            self.num = self.num + 1

    def union(self, a, b):  # 交集
        self.num = 0
        self.lst = []
        for i in range(a.num):
            if b.lst.count(a.lst[i]) == 1:
                self.lst.append(a.lst[i])
                self.num = self.num + 1

    def inter(self, a, b):  # 并集
        self.num = 0
        self.lst = []
        for i in range(a.num):
            self.lst.append(a.lst[i])
            self.num = self.num + 1
        for i in range(b.num):
            if self.lst.count(b.lst[i]) == 0:
                self.lst.append(b.lst[i])
                self.num = self.num + 1

    def delt(self, a):  # 删除元素
        self.num = self.num - 1
        self.lst.remove(a)


a = mset()
a.insert(1)
a.insert(2)
b = mset()
b.insert(1)
b.insert(3)
c = mset()
c.inter(a, b)
print(c.lst)
c.union(a, b)
print(c.lst)
c.delt(1)
c.insert(2)
print(c.lst)
