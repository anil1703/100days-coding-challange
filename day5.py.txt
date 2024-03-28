class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int: # Sliding window (similar to Leetcode 713)
        count = defaultdict(int)
        res = 0
        l = 0 # Left pointer
        for r in range(len(nums)): # Move right pointer sequentially
            count[nums[r]] += 1 # Increment the freq of current number
            while count[nums[r]] > k: # If there's a freq that needs to be checked if it's exceeded `k` or not, it's the current number cuz we've just incremented it
                count[nums[l]] -= 1 # Narrow the range and decrement the freq
                l += 1 # Move left pointer to the right -> narrow the range
            res = max(res, r - l + 1) # Always get the max result between previous and current window
        return res


"""link-https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/solutions/4935528/python-easy-approach-with-explicit-explanation/"""