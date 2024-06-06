class Solution:
    def isNStraightHand(self, hand: List[int], k: int) -> bool:
        if len(hand) % k != 0:
            return False
    
        counts = Counter(hand)
        for num in sorted(counts):
            if counts[num] > 0:
                count = counts[num]
                for i in range(num, num + k):
                    if counts[i] < count:
                        return False
                    counts[i] -= count
        
        return True