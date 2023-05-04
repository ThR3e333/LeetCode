class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [0]
        result = 0
        for i in range(1, len(height)):
            if height[i] <= height[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) != 0 and height[i] > height[stack[-1]]:
                    mid = height[stack[-1]]
                    stack.pop()
                    if len(stack)!=0:
                        h = min(height[i], height[stack[-1]])-mid
                        w = i-stack[-1]-1
                        result += h*w
                stack.append(i)
        return result