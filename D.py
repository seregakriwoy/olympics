n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

max_i, min_i = 0, 0
min_el, max_el = lst[min_i], lst[max_i]
for i in range(len(lst)):
    if lst[i] > max_el:
        max_i = i
    if lst[i] < min_el:
        min_i = i
ml = 0
gl = 0
sm = lst[max_i]
sg = lst[min_i]

left_b = 0
right_b = 0
for i in range(len(lst)):
    if max_i > min_i:
        if i > max_i:
            right_b += lst[i]
    else:
        if i < max_i:
            left_b += lst[i]
if left_b > 0:
    sm += left_b
if right_b > 0:
    sm += right_b

left_b = 0
right_b = 0
for i in range(len(lst)):
    if max_i > min_i:
        if i < min_i:
            left_b += lst[i]
    else:
        if i > min_i:
            right_b += lst[i]
if left_b < 0:
    sg += left_b
if right_b < 0:
    sg += right_b

lst_max = [0]
lst_min = [0]
sm_max = 0
sm_min = 0
if max_i > min_i:
    for i in range(min_i, max_i):
        lst_max.append(sm_max + lst[i])
    for i in range(max_i, min_i):
        lst_min.append(sm_min + lst[i])
    raz = max(lst_max) - min(lst_min)
else:
    for i in range(max_i, min_i):
        lst_max.append(sm_max + lst[i])
    for i in range(min_i, min_i):
        lst_min.append(sm_min + lst[i])
    raz = max(lst_max) - min(lst_min)

print(sm - sg + raz)
