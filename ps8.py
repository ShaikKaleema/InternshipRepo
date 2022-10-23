<<<<<<< HEAD
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
=======
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
>>>>>>> 97be87de4448efbba274d675595b0f1206059fbc
    print()