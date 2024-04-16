class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        is_prime = [True for i in range(max(nums)+1)]
        is_prime[0] = is_prime[1] = False
        n= max(nums) 

        i = 2
        while i * i <= n:
            if is_prime[i]:
                j = i * i
                while j <= n:
                    is_prime[j] = False
                    j += i
            i += 1
        left = 0
        right = 0
        diff = 0
        while right < len(nums):
            if not is_prime[nums[left]]:
                left +=1
            if is_prime[nums[left]] and is_prime[nums[right]]:
                diff = max(diff, right -left)
            right +=1
        return diff


