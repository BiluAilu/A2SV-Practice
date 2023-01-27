
s = input()
checker = 'hello'
i = 0
for c in s:
        if c == checker[i]:
                i += 1
        if i == 5:
                break
print('YES' if i == 5 else 'NO')
 



