n = int(input())

output = 1

for i in range(2, n):
    L = list(range(1, i+1))
    while sum(L) < n:
        L.pop(0)
        L.append(L[-1]+1)
    if sum(L) == n:
        output += 1

print(output)