class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count, unique, c = [], [], []

        for i in nums:
            if i not in unique:
                unique.append(i)
                c.append(nums.count(i))

        for i in range(k):
            m=max(c)
            i=c.index(m)
            count.append(unique[i])
            c[i]=-1
        return count