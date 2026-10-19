class Solution(object):
    def rotate(self, nums, k):
        n=len(nums)
        if n==0:
            return

        k=k%n

        
        nums[:]=nums[-k:]+nums[:-k] if k else nums