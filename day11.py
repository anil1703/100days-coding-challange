class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x != 0:
            m = x % 10
            x //= 10
            rev = rev * 10 + m
            if rev > 2**31 - 1:
                return 0
        
        return sign * rev
