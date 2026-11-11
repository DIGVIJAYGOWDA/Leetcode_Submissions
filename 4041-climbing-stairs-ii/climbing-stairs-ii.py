class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        costs=[0]+costs
        dp=[inf]*(n+1)
        dp[0]=0

        for i in range(1,n+1):
            if i==1:
                dp[i]=costs[i]+(i-(i-1))**2
            elif i==2:dp[i]=min(

                dp[i-1]+costs[i]+(i-(i-1))**2,
                dp[i-2]+costs[i]+(i-(i-2))**2
            )
            else:dp[i]=min(
                dp[i-1]+costs[i]+(i-(i-1))**2,
                dp[i-2]+costs[i]+(i-(i-2))**2,
                dp[i-3]+costs[i]+(i-(i-3))**2
                )
        return dp[-1]

