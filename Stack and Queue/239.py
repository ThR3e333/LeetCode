# Approach 1

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = deque()
        for i in range(k):
            while que and que[-1] < nums[i]:
                que.pop()
            que.append(nums[i])
        res = [que[0]]
        for i in range(k,len(nums)):
            if que and que[0] == nums[i-k]:
                que.popleft()
            while que and que[-1] < nums[i]:
                que.pop()
            que.append(nums[i])
            res.append(que[0])
        return res

# Approach 2

from collections import deque
class MyQueue:
    def __init__(self):
        self.que = deque()

    def pop(self, val):
        if self.que and self.que[0] == val:
            self.que.popleft()

    def push(self, val):
        while self.que and self.que[-1] < val:
            self.que.pop()
        self.que.append(val)

    def front(self):
        return self.que[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = MyQueue()
        res = []
        for i in range(k):
            que.push(nums[i])
        res.append(que.front())
        for i in range(k,len(nums)):
            que.pop(nums[i-k])
            que.push(nums[i])
            res.append(que.front())
        return res


