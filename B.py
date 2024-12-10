n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
lst.sort()
click = 0
for i in range(n):
    if i == n-1:
        click += 2
    else:
        click += lst[i] + 1
print(click)