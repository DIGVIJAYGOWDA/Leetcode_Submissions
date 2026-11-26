class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        ans = 0

        for x in s:
            if x - 1 not in s:
                y = x
                while y + 1 in s:
                    y += 1
                ans = max(ans, y - x + 1)

        return ans