n, length = map(int, input().split())
laterns = sorted(map(int, input().split()))
 
dist = 0
i, j = 0, 1
while j < n:
    dist = max(laterns[j] - laterns[i], dist)
    i += 1
    j += 1
dist = dist/2
if laterns[0] != 0:
    dist = max(dist, laterns[0])
if laterns[-1] != length:
    dist = max(dist, length - laterns[-1])
print(f'{dist:.10f}')

