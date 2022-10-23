#Odd repeat
T=int(input())
for i in range(T):
    N,K,S=map(int,input().split())
    S=S-(N*N)
    print(int(S/(K-1)))