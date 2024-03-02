
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(idx, prev, prev_sum):
            if prev_sum > target:
                return
            
            elif prev_sum == target:
                ans.add(tuple(prev))
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                
                prev.append(candidates[i])
                backtrack(i + 1, prev, prev_sum + prev[-1])
                prev.pop()

        candidates.sort()
        ans = set()
        backtrack(0, [], 0)
        
        return list(ans)
