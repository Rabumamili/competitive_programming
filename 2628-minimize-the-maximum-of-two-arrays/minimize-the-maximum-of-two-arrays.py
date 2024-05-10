class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        l, r = uniqueCnt1 + uniqueCnt2, 2 * int(1e9)

        def check(m):
            lcm = (divisor1 * divisor2) / gcd(divisor1, divisor2)
            
            cnt = m - (m // divisor1 + m // divisor2 - m // lcm)
            u1 = max(0, uniqueCnt1 - (m // divisor2 - m // lcm))
            u2 = max(0, uniqueCnt2 - (m // divisor1 - m // lcm))
            return cnt >= u1 + u2

        while l < r:
            m = (l + r) // 2
            if check(m):
                r = m
            else:
                l = m + 1
        return l