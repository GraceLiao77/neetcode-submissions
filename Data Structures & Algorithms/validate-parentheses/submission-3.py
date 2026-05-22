class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0: return False

        stack = []
        openParentheses = ['(', '[', '{']
        closeToOpen = {
            ')': '(',
            ']': '[',
            '}': '{',
        }


        for item in s:
            if item in openParentheses:
                stack.append(item)
            else:
                if stack and closeToOpen[item] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack



        
        