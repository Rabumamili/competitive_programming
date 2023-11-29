class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        k = []
        for i in strs:
            k.append(list(i)) 


        print(k)

        m =""
        if len(k) ==1 :
            if k == [ ""   ]:
                return ""
            else :
                return strs[0]
            return m
        else :  
            ini = k[0]

            for i in range(1,len(k)):
                d = k[i]
                j = 0
                while (j<min(len(d),len(ini))):
                    if (d[j] != ini[j]):
                        break
                    j +=1
                ini = ini[:j]

            return "".join(ini)    