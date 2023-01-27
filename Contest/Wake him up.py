# ####################################
# ########Others solution

# listinput = lambda : list(map(int, input().split()))
# numL, k = listinput()
# theorems = listinput()
# status = listinput()
# ans = sum(t for t,s in zip(theorems, status) if s)
 
 
# cur_window = 0
# for i in range(k):
#     if not status[i]:
#         cur_window += theorems[i]
# max_window = cur_window
# for r in range(k, numL):
#     if not status[r]:
#         cur_window += theorems[r]
#     if not status[r-k]:
#         cur_window -= theorems[r-k]
#     max_window = max(max_window, cur_window)
# print(ans + max_window)



########################################################

n, k = list(map(int, input().split()))
theo = list(map(int, input().split()))
answer = list(map(int, input().split()))
written = 0
for i in range(n):
    if theo[i] == 1:
        written += answer[i]
 
c_window = 0
for i in range(k):
    if theo[i] == 0:
        c_window += answer[i]
max = c_window
for j in range(k, n):
    if theo[j] == 0:
        c_window += answer[j]
    if theo[j - k] == 0:
        c_window -= answer[j - k]
    max = max(max, c_window)
print(written + max)