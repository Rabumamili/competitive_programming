class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq  = Counter(nums)
        srtd = sorted(freq, key=lambda x: (freq[x], -x))
        ans = []
        for num in srtd:
            while freq[num]> 0:
                ans.append(num)
                freq[num]-=1
        return ans