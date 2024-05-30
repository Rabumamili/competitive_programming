class Solution:
    def distance(self, nums: List[int]) -> List[int]:
     
        
        n = len(nums)
        idx_dict = defaultdict(list)
        
        # Collect indices for each number in nums
        for i, num in enumerate(nums):
            idx_dict[num].append(i)
        
        arr = [0] * n
        
        for idx_list in idx_dict.values():
            idx_list.sort()
            k = len(idx_list)
            
            # Prefix sums of indices
            pre_sum = [0] * (k + 1)
            for i in range(k):
                pre_sum[i + 1] = pre_sum[i] + idx_list[i]
            
            for i in range(k):
                idx = idx_list[i]
                l_sum = i * idx_list[i] - pre_sum[i]
                r_sum = (pre_sum[k] - pre_sum[i + 1]) - (k - i - 1) * idx_list[i]
                arr[idx] = l_sum + r_sum
        
        return arr
    