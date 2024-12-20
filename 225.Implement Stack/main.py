from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.top_element = None

    def push(self, x: int) -> None:
        self.q2.append(x)
        self.top_element = x
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1,self.q2 = self.q2,self.q1

    def pop(self) -> int:
        result = self.q1.popleft()
        if self.q1:
            self.top_element = self.q1[0]
        return result

    def top(self) -> int:
        return self.top_element
        

    def empty(self) -> bool:
        return not self.q1
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
