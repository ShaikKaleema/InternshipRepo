#Equality
T=int(input())
x=[]
for i in range(T):
    N=int(input())
    X=list(map(int,input().split()))
    add=sum(X)
    res=add//(N-1)
    for i in range(len(X)):
        print(res-X[i],end=" ")
    print()