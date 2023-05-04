class Solution:
    def jump(self, nums: List[int]) -> int:
        curDis, nextDis = 0, 0
        result = 0
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            nextDis = max(i+nums[i], nextDis)
            if i == curDis:
                if curDis < len(nums) - 1:
                    result += 1
                    curDis = nextDis
                    if nextDis >= len(nums) - 1:
                        break
        return result