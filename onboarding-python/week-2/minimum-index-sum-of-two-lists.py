class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        minindexSum= float('inf')
        commonStrng = []

        for i in list1:
            if i in list2:
                minindexSum = min(minindexSum, list1.index(i) + list2.index(i))

        for j in list1:

            if j in list2 and (list1.index(j) + list2.index(j))==minindexSum:
                commonStrng.append(j)
        return commonStrng



        