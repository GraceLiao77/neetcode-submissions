class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                res = int(stack.pop()) + int(stack.pop())
                stack.append(res)
            elif i == '-':
                firstPop = int(stack.pop())
                res = int(stack.pop()) - firstPop
                stack.append(res)
            elif i == '*':
                res = int(stack.pop()) * int(stack.pop())
                stack.append(res)
            elif i == '/':
                firstPop = int(stack.pop())
                res = int(stack.pop()) / firstPop
                stack.append(res)
            else:
                stack.append(i)
        
        return int(stack.pop())