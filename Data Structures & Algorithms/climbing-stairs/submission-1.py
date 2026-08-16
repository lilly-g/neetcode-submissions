class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize array of size n
        memo = [-1] * n

        def climb(i) :
            if i == n :
                return 1
            if i > n :
                return 0
            if memo[i] != -1 :
                return memo[i]
            
            memo[i] = climb(i+1) + climb(i+2)
            return memo[i]

        return climb(0)