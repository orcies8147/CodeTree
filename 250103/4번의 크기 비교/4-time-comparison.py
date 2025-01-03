a=int(input())
b,c,d,e = map(int,input().split())
L = [b,c,d,e]

for i in L:
    if a>i:
        print(1)
    else:
        print(0)