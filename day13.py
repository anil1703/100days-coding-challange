class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        A = sorted(heights)
        count = 0 
        for i in range(len(heights)):
            if heights[i] == A[i]:
                pass
            else:
                count += 1 
        return count

#https://leetcode.com/problems/height-checker/?envType=daily-question&envId=2024-06-10