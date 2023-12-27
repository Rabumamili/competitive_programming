class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        # """
        # :type arr1: List[int]
        # :type arr2: List[int]
        # :rtype: List[int]
        # """
        
        # ans =[]
        # remaining =[]
        # for nums in arr2:
        #     count = arr1.count(nums)
        #     arr = [nums]*count
        #     ans.extend(arr)
        
        # for i in range(len(arr1)):
        #     if arr1[i] not in ans:
        #         remaining.append(arr1[i])
        # remaining.sort()
        # ans.extend(remaining)
        
        # return ans
         
        #   using comparator 
        def comparator(num):
            if num in arr2:
                return arr2.index(num)
            else:
                return len(arr2) + num

        return sorted(arr1, key=comparator)


        
     
        
 
        