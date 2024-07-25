class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        d={}
        j=0
        s=[]
        ans=[]
        for i in mapping:
            d[j]=i
            j+=1
        for num in nums:
            if num==0:
                temp=d[0]
            else:
                temp=0
            mul=1
            while num>0:
                a=num%10
                a=d[a]
                temp+=a*mul
                mul=mul*10
                num=num//10
            s.append(temp)
       
        sorted_arr = [x for _, x in sorted(zip(s,nums), key=lambda pair: pair[0])]
        return sorted_arr

        