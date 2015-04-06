#queue

class Queue:
    
    def __init__(self):
        self.stack = []
    
    def push(self, a):
        self.stack.append(a)

    def pop(self):
        return self.stack.pop(0)

    def is_empty(self):
        return not self.stack
        
if __name__ == '__main__':
    
    quantum = 100
    tasks = [("p1", 150), ("p2", 80), ("p3", 200), ("p4", 350), ("p5", 20)]
    
    queue = Queue()
    for e in tasks:
        queue.push(e)
        
    elapsed_time = 0
    while not queue.is_empty():
        task = queue.pop()
        if task[1] <= quantum:
            elapsed_time += task[1]
            print("{} {}".format(task[0], elapsed_time))
        else:
            elapsed_time += quantum
            queue.push((task[0], task[1] - quantum))
