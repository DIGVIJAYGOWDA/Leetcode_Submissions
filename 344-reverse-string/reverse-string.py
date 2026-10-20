class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n=len(s)

        for i in range(n//2):
            j=n-1-i
            s[i],s[j]=s[j],s[i]