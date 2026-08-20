class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {} # min cost to climb to that stair

        def climb(i) :            
            if i == 0 :
                return cost[0]
            if i == 1 :
                return cost[1]

            if i in memo:
                return memo[i]

            if i != n :
                memo[i] = cost[i] + min(climb(i-1), climb(i-2))
            else :
                memo[i] = min(climb(i-1), climb(i-2))
            
            return memo[i]
        
        return climb(n)