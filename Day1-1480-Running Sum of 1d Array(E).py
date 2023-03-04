from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runsum = 0
        nl = []
        for el in nums:
            runsum += el
            nl.append(runsum)
        return nl