again = True
while again:
    string = input()
    n = len(string)
    if n == 0:
        break
    
    stack = []
    curlen = -1
    res = [' ' for i in range(n)]

    for i in range(n):
        if string[i] != '(' and string[i] != ')':
            continue
        elif string[i] == '(':
            if len(stack) == 0:
                stack.append([i,'('])
                curlen = curlen+1  
            else:
                if stack[curlen][1] == ')':
                    stack.pop(curlen)
                    curlen = curlen-1
                else:
                    stack.append([i,'('])
                    curlen = curlen+1  
        elif string[i] == ')':
            if len(stack) == 0:
                stack.append([i,')'])
                curlen = curlen+1  
            else:
                if stack[curlen][1] == '(':
                    stack.pop(curlen)
                    curlen = curlen-1
                else:
                    stack.append([i,')'])
                    curlen = curlen+1  
                    
    for idx,c in stack:
        if c is '(':
            res[idx] = 'x'
        else:
            res[idx] = '?'

    print(''.join(res))
