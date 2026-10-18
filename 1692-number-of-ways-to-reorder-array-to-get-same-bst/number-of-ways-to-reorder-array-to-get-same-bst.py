class Solution(object):
    def numOfWays(self, nums):
        mod = 10**9 + 7

        def dfs(nums):
            if len(nums) < 3:
                return 1

            left = [x for x in nums if x < nums[0]]
            right = [x for x in nums if x > nums[0]]

            left_ways = dfs(left)
            right_ways = dfs(right)

            ways = 1
            n = len(nums) - 1
            l = len(left)

            for i in range(1, l + 1):
                ways = ways * (n - i + 1) // i

            return (left_ways * right_ways * ways) % mod

        return (dfs(nums) - 1) % mod