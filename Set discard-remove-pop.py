n = int(input())
s = set(map(int, input().split()))
commNum = int(input())

for i in range(commNum):
    command = input()
    
    if command.split()[0] == 'pop':
        s.pop()
    if command.split()[0] == 'remove':
        s.remove(int(command.split()[1]))
    if command.split()[0] == 'discard':
        s.discard(int(command.split()[1]))
        
print(sum(s))
