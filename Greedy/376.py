class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        prediff, curdiff, result = 0, 0, 1
        if len(nums) == 1:
            return 1
        for i in range(len(nums)-1):
            curdiff = nums[i+1] - nums[i]
            if (prediff <= 0 and curdiff > 0) or (prediff >= 0 and curdiff < 0):
                result += 1
                prediff = curdiff
        return result