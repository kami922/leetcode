from collections import deque
        
class MyStack:
    def __init__(self):
        # Define the data members.
        self.data = deque()
        
    def getSize(self) -> int:
        # Implement the getSize() function.
        return len(self.data)

    def empty(self) -> bool:
        # Implement the isEmpty() function.
        return len(self.data) == 0

    def push(self, element: int) -> None:
        # Implement the push() function.
        s = len(self.data)
        self.data.append(element)
        for i in range(s):
            self.data.append(self.data.popleft()) 

    def pop(self) -> int:
        # Implement the pop() function.
        if (not self.data):
            return -1
        else:
            return self.data.popleft()

    def top(self) -> int:
        # Implement the top() function.
        if (not self.data):
            return -1
        return self.data[0]



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()