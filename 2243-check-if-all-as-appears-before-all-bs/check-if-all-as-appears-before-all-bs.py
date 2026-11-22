class Solution:
    def checkString(self, s: str) -> bool:
        flag=False
        for i in range(len(s)):
            if s[i]=='b':
                flag=True
            elif s[i]=='a' and flag: #checks True and False and if the result is False neither block executes
                return False
                
        return True