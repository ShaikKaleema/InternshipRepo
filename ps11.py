<<<<<<< HEAD
#Count palindromes
T=input()
a=len(T)
b=[1]
for i in range(1,a):
    sum=0
    for j in range(i+1):
        M=T[j:i+1]
        if M[::-1]==M:
            x=b[j-1]
            if j-1<0:
                x=1
            sum+=x
    b.append(sum)
=======
#Count palindromes
T=input()
a=len(T)
b=[1]
for i in range(1,a):
    sum=0
    for j in range(i+1):
        M=T[j:i+1]
        if M[::-1]==M:
            x=b[j-1]
            if j-1<0:
                x=1
            sum+=x
    b.append(sum)
>>>>>>> 97be87de4448efbba274d675595b0f1206059fbc
print(b[-1]%((10**9)+7))