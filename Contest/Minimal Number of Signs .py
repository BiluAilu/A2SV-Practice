####################################
########Others solution

numLine = int(input())
words = [input() for i in range(numLine)]
out=['?']*len(words[0])
for word in words:
    for index, char in enumerate(word):
        if out[index] == '?' and char != '?':
            out[index]=char
        elif out[index] != '?' and char != '?':
            if out[index] != char:
                out[index] = '0'
      
out = ''.join(out)
out = out.replace('?', 'x')
out = out.replace('0', '?')
print(out)