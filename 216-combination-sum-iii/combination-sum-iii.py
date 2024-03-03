class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        arr = []
        total = [0]
        def my(num ,path):
            if total[0] == n and len(path) == k:
                arr.append(path[:])
            elif total[0] > n:
                return
            
            for i in range(num,10):
                path.append(i)
                total[0]+=i
                my(i+1,path)
                total[0]-=i
                path.pop()
        my(1,[])
        return arr