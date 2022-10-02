# cool name
T=int(input())
for _ in range(T):
    str1=input()
    str2=sorted(str1)
    sum=0
    for i in range(len(str2)):
        sum+=(i+1)*(ord(str2[i])-96)
    print(sum)