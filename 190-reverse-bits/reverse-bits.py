class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            # Extract the last bit of n
            bit = (n >> i) & 1
            # Shift the bit to its reversed position and add to result
            result = result | (bit << (31 - i))
        return result