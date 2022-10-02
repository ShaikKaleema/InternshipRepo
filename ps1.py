#sleep deprivation
T=int(input())
l=[]
for i in range(T):
    k=int(input())
    l.append(k)
for j in range(T):
    if l[j]<7:
        print('YES')
    else:
        print('NO')