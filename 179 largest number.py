class Solution(object):

    def largestNumber(nums):

        num_strings = [str(num) for num in nums]

        for i in range(len(num_strings)):
            for j in range(i+1, len(num_strings)):
                if num_strings[i] + num_strings[j] > num_strings[j] + num_string[i]:
                    continue
                else:
                    num_strings[i], num_strings[j] = num_strings[j], num_strings[i]

        result = "".join(num_strings)

        if int(result) == 0:
            return "0"
        return result
