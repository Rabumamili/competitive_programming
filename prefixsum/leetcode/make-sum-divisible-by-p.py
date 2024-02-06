class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        n = len(nums)

        sums= sum(nums)
        if sums %p == 0:
            return 0
        reminder = sums % p
        _map = { 0 : -1}
        mod_val = 0
        result = n
        for i in range (n):
            mod_val = (mod_val + nums[i]) %p
            _map [mod_val] = i

            if (mod_val - reminder) %p in _map:
                curr = _map[(mod_val - reminder)% p]
                result= min (result , i - curr)
        return result if result < n else -1


         
        