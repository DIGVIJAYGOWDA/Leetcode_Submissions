class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        res=0
        for i in range(n):
            sub=set()
            for j in range(i,n):
                sub.add(nums[j])
                res=res+len(sub)**2
                

        return res