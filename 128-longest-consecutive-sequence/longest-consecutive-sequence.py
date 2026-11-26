class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        my_set = set()

        for i in range(len(nums)):
            my_set.add(nums[i])

        longest = 0

        for num in my_set:
            if num - 1 not in my_set:
                n = num
                count = 1

                while n + 1 in my_set:
                    count += 1
                    n += 1

                longest = max(longest, count)

        return longest