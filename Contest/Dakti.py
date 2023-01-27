####################################
########Others solution


numLine = int(input())
for _ in range(numLine):
  li = input().split()
  dic = {}
  for word in li:
    store = []
    order = 0
    for ch in word:
      if ch.isdigit():
        order = order * 10 + int(ch)
      else:
        store.append(ch)
    dic[order] = "".join(store)
  key = list(dic.keys())
  key.sort()
  final = []
  for k in key:
    final.append(dic[k])
  print(" ".join(final))