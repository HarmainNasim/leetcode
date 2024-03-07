class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[] #initialise empty stack
        for d in path.split("/"):
            if d =="":
                pass
            elif d == ".":
                pass
            elif d == "..":
                if stack:
                    stack.pop()
                else:
                    pass
            else:
                stack.append(d)
        return "/" + "/".join(stack)
        
