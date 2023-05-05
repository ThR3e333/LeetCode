class MyQueue:
    '''
    Implementing a queue using two stacks.
    '''

    def __init__(self):
        '''
        Initialize two stacks for the queue.
        '''
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        '''
        Add an element to the queue.

        :param x: The element to be added to the queue.
        '''
        self.stack_in.append(x)

    def pop(self) -> int:
        '''
        Removes and returns the front element from the queue.

        :return: The front element of the queue, if the queue is empty, returns None.
        '''
        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        else:
            # Moves elements from stack_in to stack_out in reverse order,
            # to maintain the order of elements
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self) -> int:
        '''
        Returns the front element of the queue without removing it.

        :return: The front element of the queue, if the queue is empty, returns None.
        '''
        ans = self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self) -> bool:
        '''
        Check if the queue is empty.

        :return: True if the queue is empty, False otherwise.
        '''
        return not (self.stack_in or self.stack_out)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()