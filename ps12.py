<<<<<<< HEAD
#Bitwise tuples
T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    comp=pow(2,N,10**9+7)-1
    res=pow(comp,M,10**9+7)
=======
#Bitwise tuples
T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    comp=pow(2,N,10**9+7)-1
    res=pow(comp,M,10**9+7)
>>>>>>> 97be87de4448efbba274d675595b0f1206059fbc
    print(res)