class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = []
        left = 0
        right = n
        while right < len(nums):
            answer.append(nums[left])
            answer.append(nums[right])
            left += 1
            right += 1
        return answer


        

        