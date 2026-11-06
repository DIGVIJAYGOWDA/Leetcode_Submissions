class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n=len(nums)
        curr_sum=0
        

        for i in range(k):
            curr_sum+=nums[i]
        max_avg=curr_sum/k

        for i in range(k,n):
            curr_sum+=nums[i]
            curr_sum-=nums[i-k]
            avg=curr_sum/k
            max_avg=max(max_avg,avg)

        return max_avg