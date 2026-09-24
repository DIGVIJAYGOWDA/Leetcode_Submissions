class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i,nums in enumerate(nums):
            s=0
            while nums:
                s+=nums%10
                nums//=10
            if s==i:
                return i
        return -1