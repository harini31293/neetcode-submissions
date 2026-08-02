class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev={}
        for i, j in enumerate (nums):
            res= target - j
            if res in prev:
                return [prev[res], i]
            prev[j] =i
        