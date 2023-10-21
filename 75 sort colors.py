class Solution(object):

    def sortColors(self, nums):

        start = 0
        mid = 0
        end = len(nums) - 1

        while mid <= end:

            if nums[mid] == 0:

                self.swap(nums, start, mid)
                mid += 1
                start += 1

            elif nums[mid] == 1:
                mid += 1

            elif nums[mid] == 2:

                self.swap(nums, mid, end)
                end -= 1

    def swap(self, arr, pos1, pos2):
        temp = arr[pos1]
        arr[pos1] = arr[pos2]
        arr[pos2] = temp
