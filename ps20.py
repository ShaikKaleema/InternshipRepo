'''Problem statement :
Mike likes strings. He is also interested in algorithms. A few days ago he discovered for himself a very nice problem:
You are given an AB-string S. You need to count the number of substrings of S, which have an equal number of 'A'-s and 'B'-s.
Do you know how to solve it? Good. Mike will make the problem a little bit more difficult for you.
You are given an ABC-string S. You need to count the number of substrings of S, which have an equal number of 'A'-s, 'B'-s and 'C'-s.
A string is called AB-string if it doesn't contain any symbols except 'A' or 'B'. A string is called ABC-string if it doesn't contain any symbols except 'A', 'B' or 'C'.

Input
The first line of the input contains an ABC-string S.

Output
Your output should contain the only integer, denoting the number of substrings of S, which have an equal number of 'A'-s, 'B'-s and 'C'-s.
The answer can go above a 32-bit int'''

#code 

s=input()
dicti={}
dicti[(0,0)]=1
a=b=c=0
res=0
for i in s:
    if i=='A':
        a+=1
    elif i=='B':
        b+=1
    elif i=='C':
        c+=1
    ans=(a-b,a-c)
    if ans in dicti:
        res+=dicti[ans]
    dicti[ans]=dicti.get(ans,0)+1
print(res)

