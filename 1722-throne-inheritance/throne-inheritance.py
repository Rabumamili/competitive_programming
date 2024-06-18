class ThroneInheritance:
    def __init__(self, kingName: str):
        self.king = kingName
        self.children = {kingName: []}
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        if parentName in self.children:
            self.children[parentName].append(childName)
        else:
            self.children[parentName] = [childName]
        self.children[childName] = []

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> list:
        order = []
        self._dfs(self.king, order)
        return order

    def _dfs(self, current: str, order: list) -> None:
        if current not in self.dead:
            order.append(current)
        for child in self.children[current]:
            self._dfs(child, order)


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()