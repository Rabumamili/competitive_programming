class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last_index = {}
        res = float('inf')
        for idx in range(len(cards)):
            if cards[idx] in last_index:
                res = min(res, idx - last_index[cards[idx]] + 1)
            last_index[cards[idx]] = idx
       
        return res if res != float('inf') else -1
             