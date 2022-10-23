<<<<<<< HEAD
#Odd repeat
T=int(input())
for i in range(T):
    N,K,S=map(int,input().split())
    S=S-(N*N)
=======
#Odd repeat
T=int(input())
for i in range(T):
    N,K,S=map(int,input().split())
    S=S-(N*N)
>>>>>>> 97be87de4448efbba274d675595b0f1206059fbc
    print(int(S/(K-1)))