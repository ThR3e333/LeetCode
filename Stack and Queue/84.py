class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [0]
        result = 0
        heights.append(0)
        heights.insert(0,0)
        for i in range(1, len(heights)):
            if heights[i] >= heights[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) != 0 and heights[i] < heights[stack[-1]]:
                    mid = stack[-1]
                    stack.pop()
                    if stack:
                        left = stack[-1]
                        right = i
                        h = heights[mid]
                        w = right-left-1
                        result = max(result, h*w)
                stack.append(i)
        return result