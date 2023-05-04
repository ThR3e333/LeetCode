# Approach 1

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, cover = 0, 0
        while i <= cover:
            cover = max(i + nums[i], cover)
            if cover >= len(nums) - 1:
                return True
            i += 1
        return False

# Approach 2

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        if len(nums) == 1:
            return True
        for i in range(len(nums)):
            if i <= cover:
                cover = max(i+nums[i], cover)
                if cover >= len(nums) - 1:
                    return True
        return False
