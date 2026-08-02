class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i, j in enumerate(nums):
            look = target - nums[i]
            if look in res:
                return([res[look],i])
            res[j] = i