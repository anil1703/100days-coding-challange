class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        n = 0 
        for i in gain:
            res += i 
            n = max(n,res)
        return n
                
        