class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l =0 
        countB = 0
        countW = 0 
        result = len(blocks)+1

        for r in range(len(blocks)):
            ch = blocks[r]
            if ch=="B": countB +=1
            else: countW += 1
            if countB+countW>=k:
                result = min(result, countW)
                while countB+countW>=k:
                    result = min(result, countW)
                    if blocks[l] == "B": countB -= 1
                    else: countW -= 1 
                    l+=1  
     
        return result if result>0 else 0
        