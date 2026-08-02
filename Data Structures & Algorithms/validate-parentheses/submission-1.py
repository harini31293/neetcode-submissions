class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_bracs = { ")" : "(" , "]" :"[", "}":"{" }
        for i in s:
            if i in dict_bracs:
                if stack and stack[-1] == dict_bracs[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False


        