class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastWord = s.split()
        ans = lastWord[-1]
        if(len(lastWord)==0):
            return 0 
        else:
            return len(ans)


""" Link: https://leetcode.com/problems/length-of-last-word/"""