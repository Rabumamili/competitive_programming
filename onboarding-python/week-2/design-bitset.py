class Bitset:
    def __init__(self, size: int):
        self.size = size
        self.ones = set()
        self.zeros = set(range(size))
        self.res = ['0'] * size

    def fix(self, idx: int) -> None:
        if idx in self.zeros:
            self.zeros.remove(idx)
        self.ones.add(idx)

    def unfix(self, idx: int) -> None:
        if idx in self.ones:
            self.ones.remove(idx)
        self.zeros.add(idx)

    def flip(self) -> None:
        self.ones, self.zeros = self.zeros, self.ones

    def all(self) -> bool:
        return len(self.zeros) == 0

    def one(self) -> bool:
        return len(self.ones) > 0

    def count(self) -> int:
        return len(self.ones)

    def toString(self) -> str:
        for i in range(self.size):
            if i in self.ones:
                self.res[i] = "1"
            else:
                self.res[i] = "0"
        return "".join(self.res)