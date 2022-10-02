#Maximum value
T=int(input())
for i in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    A.sort()
    print(max(A[0]*A[1]+abs(A[0]-A[1]),A[-1]*A[-2]+abs(A[-1]-A[-2])))