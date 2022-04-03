# https://leetcode.com/problems/implement-queue-using-stacks/


class MyQueue:

    def __init__(self):
        self.l1 = []
        self.l2 = []

    def push(self, x: int) -> None:
        
        if not self.l1 and not self.l2:
            self.l1.append(x)
            return
        
        print(self.l1,self.l2)
        
        
        while self.l1: # transfer elements
            ele = self.l1.pop()
            self.l2.append(ele)
            
        self.l1.append(x)

        
        while self.l2:
            ele = self.l2.pop()
            self.l1.append(ele)

    def pop(self) -> int:
        
        return self.l1.pop()
        
        

    def peek(self) -> int:

        ele = self.l1.pop()
        self.l1.append(ele)
        return ele

    def empty(self) -> bool:
        
        if not self.l1 :
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
