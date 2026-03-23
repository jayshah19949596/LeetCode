class MyQueue:

    def __init__(self):
        """
        Initialize the two stacks and a front pointer.
        'stack' will always store elements in FIFO order.
        'aux_stack' is used temporarily during the push operation.
        """
        self.stack = []
        self.aux_stack = []
        self.front = None
        
    def push(self, x: int) -> None:
        """
        Pushes element x to the back of the queue.
        Time Complexity: O(n) - We move all elements twice.
        """
        # If this is the first element, it is the front of the queue
        if not self.stack: 
            self.front = x
            
        # 1. Empty the main stack into the auxiliary stack
        while self.stack:
            self.aux_stack.append(self.stack.pop())
            
        # 2. Add the new element to the bottom of the "new" queue
        self.aux_stack.append(x)
        
        # 3. Move everything back to 'stack'. 
        # This reverses the order so the oldest element is on top.
        while self.aux_stack:
            self.stack.append(self.aux_stack.pop())
        
    def pop(self) -> int:
        """
        Removes the element from the front of the queue and returns it.
        Time Complexity: O(1) - The front is already at the top of the stack.
        """
        popped_element = self.stack.pop()
        
        # Update the front pointer to the next element in line
        if self.stack: 
            self.front = self.stack[-1]
        else: 
            self.front = None
            
        return popped_element

    def peek(self) -> int:
        """
        Returns the element at the front of the queue without removing it.
        """
        return self.front

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack) == 0
