class OrderedStream:
    def __init__(self, n: int):
        self.dic = {}
        self.i = 0
        self.n = n

    def insert(self, idKey: int, value: str) -> List[str]:
        if idKey - 1 not in self.dic:
            self.dic[idKey - 1] = []
        self.dic[idKey - 1].append(value)
        ans = []
        while self.i < self.n:
            if self.i in self.dic and self.dic[self.i]:
                ans.extend(self.dic[self.i])
                self.dic[self.i] = []
                self.i += 1
            else:
                break 
        return ans

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)