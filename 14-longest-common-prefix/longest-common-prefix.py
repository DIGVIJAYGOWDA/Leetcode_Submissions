class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not str:
            return ""

        res=""
        min_len=min(len(s)for s in strs)
        for i in range(min_len):
            for j in range(1,len(strs)):
                if strs[j][i]!=strs[0][i]:
                    return res
            res=res+strs[0][i]
        return res