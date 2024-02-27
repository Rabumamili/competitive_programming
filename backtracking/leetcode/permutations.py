class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def generate(start):
            if start == len(nums):
                permutations.append(nums[:])
                 
            else:
                for i in range(start, len(nums)):
                    # swapping
                    nums[i], nums[start] = nums[start], nums[i]
                    
                    generate(start+1)
                    # revert the swapping process
                    nums[i], nums[start] = nums[start], nums[i]
                    

        permutations = []
        generate(0)
        return permutations

      