class Solution:
    def deckRevealedIncreasing(self, deck):
        dq = []
        deck.sort(reverse=True)

        # Rotate and append each card to the left of the deque
        for card in deck:
            if dq:
                dq.insert(0, dq.pop())
            dq.insert(0, card)

        return dq