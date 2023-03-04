class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2]
        
        for i in range(3, n+1):
            dp.append(dp[i-2] + dp[i-1])
            
        return dp[n]
        #### other solution ######
        # step1 , step2 = 1,1
        # for i in range(n-1):
        #     temp = step1
        #     step1 = step1+step2
        #     step2 =temp
        # return step1


n =5 
s=Solution()
print(s.climbStairs(n))