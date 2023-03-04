from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
       S = sum(nums)
       lsum = 0
       for i , y in enumerate(nums):
        if lsum == (S - lsum - y):
            return i
        lsum +=y
       return -1

nums = [1,7,3,6,5,6]
s =Solution()
print(s.pivotIndex(nums)) 
