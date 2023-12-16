

class ATM:
    def __init__(self):
        self.arr = [0, 0, 0, 0, 0]
        self.d = {0: 20, 1: 50, 2: 100, 3: 200, 4: 500}

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.arr[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        ans = [0] * len(self.arr)

        for k in range(len(self.arr) - 1, -1, -1):
            note = self.d[k]
            if amount >= note and self.arr[k]:
                withdraw_count = min(amount // note, self.arr[k])
                ans[k] = withdraw_count
                amount -= note * withdraw_count

        if amount == 0:
            for i in range(len(self.arr)):
                self.arr[i] -= ans[i]
            return ans
        else:
            return [-1]
# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)