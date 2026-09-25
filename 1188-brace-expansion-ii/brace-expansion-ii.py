class Solution:
    def braceExpansionII(self, expression):
        stack = []
        
        for ch in expression:
            if ch == '{':
                stack.append(ch)
            
            elif ch == ',':
                stack.append(ch)
            
            elif ch == '}':
                current = set()
                
                while stack[-1] != '{':
                    part = stack.pop()
                    
                    if part == ',':
                        stack.append(current)
                        current = set()
                    else:
                        current |= part
                
                stack.pop()
                
                if stack and stack[-1] != ',' and stack[-1] != '{':
                    prev = stack.pop()
                    current = {a + b for a in prev for b in current}
                
                stack.append(current)
            
            else:
                if stack and isinstance(stack[-1], set):
                    prev = stack.pop()
                    stack.append({s + ch for s in prev})
                else:
                    stack.append({ch})
        
        result = set()
        current = set()
        
        while stack:
            part = stack.pop()
            
            if part == ',':
                result |= current
                current = set()
            else:
                if not current:
                    current = part
                else:
                    current = {a + b for a in part for b in current}
        
        result |= current
        
        return sorted(result)