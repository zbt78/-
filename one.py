source = input()
target = input()

res = 1

j = 0

i = 0
while i < len(target):
    if source.find(target[i]) == -1:
        res = -1
        break
    
    while j < len(source) and source[j] != target[i]:
        j = j+1
        
    if j >= len(source):
        res = res+1
        j = 0
    else:
        i = i+1
        
print(f"res:{res}")
