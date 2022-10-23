<<<<<<< HEAD
#Maximum value
T=int(input())
for i in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    A.sort()
=======
#Maximum value
T=int(input())
for i in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    A.sort()
>>>>>>> 97be87de4448efbba274d675595b0f1206059fbc
    print(max(A[0]*A[1]+abs(A[0]-A[1]),A[-1]*A[-2]+abs(A[-1]-A[-2])))