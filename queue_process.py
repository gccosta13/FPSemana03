from collections import deque
stack=deque()
plvrs=input()
for i in plvrs.split():
    stack.append(i)
print(stack)

while stack:
    palavra=stack.pop()
    if 'a' in palavra:
        print (palavra)