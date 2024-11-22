from collections import deque
stack=deque()
nmrs=input()
for i in nmrs.split():
    stack.append(int(i))
    
print(stack)

while stack:
    resultado=stack.pop()
    print(resultado*2)