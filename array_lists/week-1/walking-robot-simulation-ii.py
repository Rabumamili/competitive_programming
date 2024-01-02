class Robot:

    def __init__(self, width: int, height: int):
        self.x = 0
        self.y = 0
        self.w = width
        self.h = height
        self.dir = 0
        self.dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        self.d = ["East", "North", "West", "South"]
    def step(self, num: int) -> None:
        num %= (self.w - 1 + self.h - 1) * 2
        if num == 0:
            num += (self.w -1 + self.h -1) * 2

        for i in range(num):
            nx, ny = self.x + self.dirs[self.dir][0], self.y + self.dirs[self.dir][1]

            while not (0 <= nx < self.w and 0<=ny<self.h):
                self.dir = (self.dir + 1) % 4
                nx, ny = self.x + self.dirs[self.dir][0], self.y + self.dirs[self.dir][1]
            self.x, self.y = nx, ny



    def getPos(self) -> List[int]:
        return [self.x, self.y]      

    def getDir(self) -> str:
        return self.d[self.dir]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()