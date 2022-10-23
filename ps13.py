<<<<<<< HEAD
#Team formation
T=int(input())
for i in range(T):
    N=int(input())
    S=input()
    T=input()
    res=min(S.count('1'),T.count('1'),N//2)
=======
#Team formation
T=int(input())
for i in range(T):
    N=int(input())
    S=input()
    T=input()
    res=min(S.count('1'),T.count('1'),N//2)
>>>>>>> 97be87de4448efbba274d675595b0f1206059fbc
    print(res)