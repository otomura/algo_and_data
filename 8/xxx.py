#stack

expression = "1 2 + 3 4 - *"

class Stack:
    
    def __init__(self):
        self.stack = []
    
    def push(self, a):
        self.stack.append(a)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return not self.stack
        
if __name__ == '__main__':
    
    stack = Stack()
    for e in expression.split(" "):
        if e == "*":
            stack.push(int(stack.pop()) * int(stack.pop()))
        elif e == "+":
            stack.push(int(stack.pop()) + int(stack.pop()))
        elif e == "-":
            stack.push(- int(stack.pop()) + int(stack.pop()))
        else:
            stack.push(e)
    print("result is " + str(stack.pop()))
