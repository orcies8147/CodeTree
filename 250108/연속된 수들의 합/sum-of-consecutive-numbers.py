n = int(input())

output = 1

for i in range(2, n):
    S = int(i * (i-1) / 2)
    if (n-S)%i == 0:
        output+=1
    if S+i>n-1:
        break

print(output)    