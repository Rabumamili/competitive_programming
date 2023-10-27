def maxSumRangeQuery(nums, requests):
    n = len(nums)
    count = [0] * n

    # Count the number of requests that include each index
    for start, end in requests:
        count[start] += 1
        if end + 1 < n:
            count[end + 1] -= 1

    # Calculate the prefix sum of the counts
    for i in range(1, n):
        count[i] += count[i - 1]

    # Sort the nums array and the counts array in descending order
    nums.sort(reverse=True)
    count.sort(reverse=True)

    # Calculate the maximum total sum modulo 10^9 + 7
    mod = 10**9 + 7
    total_sum = 0
    for i in range(n):
        total_sum = (total_sum + nums[i] * count[i]) % mod

    return total_sum
