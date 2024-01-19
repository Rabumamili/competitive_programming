class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def getNextIndex(i):
            n = len(nums)
            return (i + nums[i]) % n
            
        for i in range(len(nums)):
            slow = i
            fast = i

            # Check for positive or negative cycle
            while nums[slow] * nums[getNextIndex(slow)] > 0 and nums[fast] * nums[getNextIndex(fast)] > 0:
                slow = getNextIndex(slow)
                fast = getNextIndex(getNextIndex(fast))

                if slow == fast:
                    # Cycle detected
                    if slow == getNextIndex(slow):
                         
                        break
                    return True

            j = i
            while nums[j] * nums[getNextIndex(j)] > 0:
                nextj = getNextIndex(j)
                nums[j] = 0
                j = nextj

        return False