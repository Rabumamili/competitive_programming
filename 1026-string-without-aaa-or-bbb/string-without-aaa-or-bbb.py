class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        result = ''
        while a > 0 and b > 0:
            if a > b:
                result += 'a'
                a -= 1
                if result[-2:] == 'aa': 
                    result += 'b'
                    b -= 1
            else:
                result += 'b'
                b -= 1
                if result[-2:] == 'bb':
                    result += 'a'
                    a -= 1

        result += 'a' * a + 'b' * b

        return result