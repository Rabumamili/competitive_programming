class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
         
        lessnums = []
        greaternums = []
        equalnums = []

        for num in nums:
            if num < pivot:
                lessnums.append(num)
            elif num > pivot:
                greaternums.append(num)
            else:
                equalnums.append(num)

        return lessnums + equalnums + greaternums
            


            