class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            digit_sum=sum(map(int, str(nums[i])))

            if digit_sum==i:
                return i

        return -1