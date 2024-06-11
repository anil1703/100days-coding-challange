class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        Ans = []
        for i in range(len(arr2)):
            if arr2[i] in arr1:
                A = arr1.count(arr2[i])
                for j in range(A):
                    Ans.append(arr2[i])
        B = []
        for i in arr1:
            if i  not in Ans:
                B.append(i)
        C= sorted(B)

        D = Ans + C
        print(D)
        return D
            
#https://leetcode.com/problems/relative-sort-array/