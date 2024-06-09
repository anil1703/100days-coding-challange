class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num  # Update first if num is smaller
            elif num <= second:
                second = num  # Update second if num is in between first and second
            else:
                return True  # If we find a number greater than both first and second
        
        return False