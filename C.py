p, q = int(input()), int(input())
treu = 0
l_pair = []
for a in range(p, q+1):
    for b in range(p, q + 1):
        for c in range(p, q + 1):
            lst = [a, b, c]
            lst.sort()
            if lst in l_pair:
                continue
            else:
                if (a < b+c) and (b < a+c) and (c < a+b):
                    treu += 1
                    l_pair.append(lst)
print(treu)