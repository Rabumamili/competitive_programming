class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for passenger in details:
            if int(passenger[11:13]) > 60:
                count += 1
        return count