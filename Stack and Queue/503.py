# Approach 1

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = [0]
        n = len(nums)
        result = [-1]*(2*n)
        nums = nums + nums
        for i in range(1, len(nums)):
            if nums[i]<=nums[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) != 0 and nums[i]>nums[stack[-1]]:
                    result[stack[-1]] = nums[i]
                    stack.pop()
                stack.append(i)
        return result[:n]

# Approach 2

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = [0]
        result = [-1]*len(nums)
        for i in range(1, 2*len(nums)):
            if nums[i%len(nums)]<=nums[stack[-1]]:
                stack.append(i%len(nums))
            else:
                while len(stack) != 0 and nums[i%len(nums)]>nums[stack[-1]]:
                    result[stack[-1]] = nums[i%len(nums)]
                    stack.pop()
                stack.append(i%len(nums))
        return result