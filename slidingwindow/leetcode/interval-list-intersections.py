class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        left = 0
        right = 0
        res = []

        while left < len(firstList) and right < len(secondList):
            temp = [max(firstList[left][0], secondList[right][0]),
                    min(firstList[left][1], secondList[right][1])]
            if temp[0] <= temp[1]:
                res.append(temp)
            if firstList[left][1] <= secondList[right][1]:
                left += 1
            else:
                right += 1

        return res
