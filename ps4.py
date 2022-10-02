#Break the stick
T=int(input())
for i in range(T):
    N,X=map(int,input().split())
    if N%2==0:
        print('YES')
    else:
        if X%2==0:
            print('NO')
        else:
            print('YES')
    