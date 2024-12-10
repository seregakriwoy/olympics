import math


a, h, k, m, s = int(input()), int(input()), int(input()), int(input()), int(input())
unp = h/k
if h%k !=0:
    ost = k - h%k
else:
    ost = 0
od_opk = k*unp+ost
kol_vert = s // od_opk
kol = a/m
print(math.ceil(kol/kol_vert))

