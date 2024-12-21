class IBList:
    def __init__(self):
        self.list = []

    def get(self,r):
        if(r < 0 or r>=len(self.list)):
            return "Index Error"
        return self.list[r]

    def set(self, r, e):
        if(r < 0 or r>=len(self.list)):
            return "Index Error"
        temp = self.list[r]
        self.list[r] = e
        return temp

    def add(self, r, e):
        if(r < 0 or r>len(self.list)):
            return "Index Error"
        self.list.insert(r, e)

    def remove(self,r):
        if(r < 0 or r>=len(self.list)):
            return "Index Error"
        temp = self.list[r]
        del self.list[r]
        return temp

    def getList(self):
        return self.list

# tests:
if __name__ == '__main__':
    iblist = IBList()
    print(iblist.add(0,'A'))
    print(iblist.getList())
    print(iblist.add(0,'B'))
    print(iblist.getList())
    print(iblist.get(1))
    print(iblist.getList())
    print(iblist.set(2,'C'))
    print(iblist.getList())
    print(iblist.add(2,'C'))
    print(iblist.getList())
    print(iblist.add(4,'D'))
    print(iblist.getList())
    print(iblist.remove(1))
    print(iblist.getList())
    print(iblist.add(1,'D'))
    print(iblist.getList())
    print(iblist.add(1,'E'))
    print(iblist.getList())
    print(iblist.get(4))
    print(iblist.getList())
    print(iblist.add(4,'F'))
    print(iblist.getList())
    print(iblist.set(2,'G'))
    print(iblist.getList())
    print(iblist.get(2))
    print(iblist.getList())