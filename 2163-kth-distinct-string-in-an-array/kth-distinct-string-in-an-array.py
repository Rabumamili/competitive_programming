class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}
        for string in arr:
            if string in count:
                count[string] += 1
            else:
                count[string] = 1
       
        distinct_strings = []
        for string in arr:
            if count[string] == 1:
                distinct_strings.append(string)

        if k <= len(distinct_strings):
            return distinct_strings[k - 1]
        else:
            return ""