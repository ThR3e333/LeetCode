# Approach 1

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        Returns the maximum element of each sliding window of size k in the given list of integers.

        :param nums: A list of integers.
        :param k: The size of sliding window.
        :return: A list of maximum element of each sliding window of size k.
        '''
        # Initialize a deque to store the indices of elements in the current sliding window
        # such that the leftmost index corresponds to the maximum element in the window
        que = deque()

        for i in range(k):
            # Remove indices from the deque whose corresponding elements are smaller than the current element nums[i]
            while que and nums[que[-1]] < nums[i]:
                que.pop()

            # Append the index of current element to the deque
            que.append(i)

        # Initialize a list to store the maximum element of each sliding window
        result = [nums[que[0]]]

        for i in range(k, len(nums)):
            # If the leftmost index in the deque is outside the current sliding window, remove it from the deque
            if que and que[0] == i-k:
                que.popleft()

            # Remove indices from the deque whose corresponding element are smaller than the current element nums[i]
            while que and nums[que[-1]] < nums[i]:
                que.pop()

            # Append the index of current element to the deque
            que.append(i)

            # Append the maximum element of the current sliding window to the result list
            result.append(nums[que[0]])

        return result

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


