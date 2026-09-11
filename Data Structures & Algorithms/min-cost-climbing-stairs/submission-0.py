class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one = 0
        two = 0

        for i in range(2,len(cost) +1):
            current = min(cost[i-1]+one, cost[i-2]+two)

            two = one
            one = current
        return one


        