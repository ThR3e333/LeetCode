from collections import deque
class MyStack:
    '''
    Implementing a stack using a queue.
    '''

    def __init__(self):
        '''
        Initialize an empty queue.
        '''
        self.que = deque()

    def push(self, x: int) -> None:
        '''
        Pushes an element onto the top of the stack.

        :param x: The element to be push onto the top of the stack.
        '''
        self.que.append(x)

    def pop(self) -> int:
        '''
        Removes and returns the top element of the stack.

        :return: The top element of the stack, if the stack is empty, return None.
        '''
        if self.empty():
            return None

        # Moves all elements except the last one to the end of the queue
        for i in range(len(self.que)-1):
            self.que.append(self.que.popleft())

        # Removes and returns the last element of the queue which is the top of the stack
        return self.que.popleft()

    def top(self) -> int:
        '''
        Returns the top element of the stack without removing it.

        :return: The top element of the stack, if the stack is empty, returns None.
        '''
        if self.empty():
            return None
        return self.que[-1]

    def empty(self) -> bool:
        '''
        Check if the stack is empty.

        :return: True if the stack is empty, False otherwise.
        '''
        return not self.que


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()