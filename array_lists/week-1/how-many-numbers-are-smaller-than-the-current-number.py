class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result=[]
        freq={}
        temp=sorted(nums)  
        
        for i in range(len(temp)): 
            if temp[i] not in freq:
                        freq[temp[i]]=i    
        for i in range(len(nums)): 
             
            result.append(freq[nums[i]])

        return result 