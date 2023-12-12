# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         left= 0
#         right = len(nums) - 1                   
#         while left < right:
#             curSum = nums[left] + nums[right]
#             if curSum ==target:
#                 return [left, right]
#             elif curSum < target:
#                 left += 1
#             else:
#                 right -= 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums_sorted = sorted(nums)  # Sort the nums list
#         left = 0
#         right = len(nums_sorted) - 1
#         while left < right:
#             curSum = nums_sorted[left] + nums_sorted[right]
#             if curSum == target:
                 
#                 return [left, right]
#             elif curSum < target:
#                 left += 1
#             else:
#                 right -= 1
#         return []
                