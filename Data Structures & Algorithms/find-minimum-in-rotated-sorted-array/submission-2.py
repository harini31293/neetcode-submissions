class Solution:
    def findMin(self, nums: List[int]) -> int:
        l =0
        h = len(nums) -1
        res = nums[0]

        while l <=h:
            if nums[l] <= nums[h]:
                res =min(res,nums[l])
                break

            mid = (l+h)//2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid+1
            else:
                h = mid -1
        return res