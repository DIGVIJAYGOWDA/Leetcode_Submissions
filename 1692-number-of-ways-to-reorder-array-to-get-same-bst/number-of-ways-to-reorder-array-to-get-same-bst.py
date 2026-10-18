class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mod = 10**9 + 7

        def combination(n, r):
            result = 1
            for i in range(r):
                result = result * (n - i) // (i + 1)
            return result

        def dfs(nums):
            n = len(nums)

            if n < 3:
                return 1

            left_nodes = [a for a in nums if a < nums[0]]
            right_nodes = [a for a in nums if a > nums[0]]

            left_ways = dfs(left_nodes)
            right_ways = dfs(right_nodes)

            ways = combination(n - 1, len(left_nodes))

            return (left_ways * right_ways * ways) % mod

        return (dfs(nums) - 1) % mod