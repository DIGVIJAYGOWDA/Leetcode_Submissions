class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]

        for ch in s:
            if ch=='(':
                stack.append(')')
            elif ch=='[':
                stack.append(']')
            elif ch=='{':
                stack.append('}')
            else:
                if not stack or stack.pop()!=ch:
                    return False

        return len(stack)==0