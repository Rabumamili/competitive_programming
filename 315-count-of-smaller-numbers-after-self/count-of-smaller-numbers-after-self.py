from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sortedarr= SortedList()
        ans = []
        for num in nums[::-1]:
            idx = sortedarr.bisect_left(num)
            ans.append(idx)
            sortedarr.add(num)
        return ans[::-1]


         












        # s = SortedList()
        # output = []
        # for n in nums[::-1]:
        #     ans = SortedList.bisect_left(s, n)
        #     output.append(ans)
        #     SortedList.add(n)
        # return output[::-1]