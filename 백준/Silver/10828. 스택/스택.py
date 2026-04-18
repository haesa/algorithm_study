import sys

class Stack:
    def __init__(self):
        self.list = []
    
    def push(self, item):
        self.list.append(item)
        
    def pop(self):
        if self.empty():
            return -1
        
        return self.list.pop()
    
    def size(self):
        return len(self.list)
    
    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0
        
    def top(self):
        if self.empty():
            return -1
        
        return self.list[-1]
    
stack = Stack()
output = []

n = int(sys.stdin.readline())

for i in range(n):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == 'push':
        stack.push(int(cmd[1]))
    elif cmd[0] == 'pop':
        output.append(str(stack.pop()))
    elif cmd[0] == 'size':
        output.append(str(stack.size()))
    elif cmd[0] == 'empty':
        output.append(str(stack.empty()))
    elif cmd[0] == 'top':
        output.append(str(stack.top()))

sys.stdout.write("\n".join(output))