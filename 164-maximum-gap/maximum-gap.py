class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        min_num, max_num = min(nums), max(nums)
        
        if max_num == min_num:
            return 0

        n = len(nums)
        bucket_size = max(1, (max_num - min_num) // (n - 1))
        bucket_count = (max_num - min_num) // bucket_size + 1
        
        buckets = [{'min': float('inf'), 'max': float('-inf')} for _ in range(bucket_count)]

        for num in nums:
            buck_idx = (num - min_num) // bucket_size
            buckets[buck_idx]['min'] = min(buckets[buck_idx]['min'], num)
            buckets[buck_idx]['max'] = max(buckets[buck_idx]['max'], num)

        max_gap = 0
        prev_max = min_num

        for bucket in buckets:
            if bucket['min'] == float('inf'):
                continue
            max_gap = max(max_gap, bucket['min'] - prev_max)
            prev_max = bucket['max']

        return max_gap
