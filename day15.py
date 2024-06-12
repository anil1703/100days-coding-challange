class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = set(nums)
        b = list(a)
        for i in b:
            A =nums.count(i)
            for j in range(A):
                nums.remove(i)
                nums += [i]
        
            

        


                

        