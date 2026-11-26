class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        my_set = set(nums)
        longest = 0

        for num in my_set:

            # Identify the starting element of a sequence
            if num - 1 not in my_set:

                count = 1
                current = num

                # Count consecutive elements
                while current + 1 in my_set:
                    current += 1
                    count += 1

                longest = max(longest, count)

        return longest