from operator import add, sub, mul
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hash_map = {'+':add, '-':sub, '*':mul, '/':lambda x,y : int(x/y)}
        stack = []
        for i in tokens:
            if i not in hash_map.keys():
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(hash_map[i](b,a))
        return stack.pop()