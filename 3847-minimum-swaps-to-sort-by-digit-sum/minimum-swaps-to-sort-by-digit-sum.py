class Solution(object):
    def minSwaps(self, nums):
        initial={n:i for i, n in enumerate(nums)}

        def helper(x):
            total=0
            while x:
                total+=x%10
                x=x//10
            return total

        nums.sort(key=lambda x:(helper(x),x))

        visited=set()
        res=0

        for i in range(len(nums)):
            if i in visited:
                continue

            j=i
            step=0

            while j not in visited:
                visited.add(j)
                step+=1
                j=initial[nums[j]]
            
            res+=step-1

        return res