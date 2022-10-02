# palindrome pain
T=int(input())
for i  in range(T):
    X,Y=map(int,input().split())
    a='a'*(X//2)
    b='b'*(Y//2)
    if (X==1 or Y==1):
        print(-1)
    elif( X%2==1 and Y%2==1):
        print(-1)
    elif (X%2==0 and Y%2==0):
        print(a+'b'*Y+a)
        print(b+'a'*X+b)
    elif(X%2==0):
        print(a+'b'*Y+a)
        print(b+a+'b'+a+b)
    elif (Y%2==0):
        print(b+'a'*X+b)
        print(a+b+'a'+b+a)