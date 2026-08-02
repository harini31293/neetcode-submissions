class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <=r:
            mid = (l+r)//2
            total = sum(math.ceil(pile/mid) for pile in piles)
            if total > h:
                #res = mid
                l = mid + 1
            else:
                r = mid - 1
                res = mid
        return res
            

        