'''
Problem statement 
You are given a string SS with length NN and you should change it to a palindrome using a sequence of zero or more operations. In one operation, you should choose two adjacent elements of SS (two characters) and swap them; however, neither of these elements may be used in any other operation.
Find the minimum number of operations you have to perform in order to change the string SS into a palindrome, or determine that it is impossible.

Input
The first line of the input contains a single integer TT denoting the number of test cases. The description of TT test cases follows.
The first line of each test case contains a single integer NN.
The second line contains a single string SS with length NN.

Output
For each test case:
If it is impossible to make the string SS a palindrome, print a single line containing the string "NO" (without quotes).
Otherwise, print two lines. The first of these lines should contain the string "YES" (without quotes). The second line should contain a single integer ― the minimum required number of operations.'''

#code

T=int(input())
for _ in range(T):
    n=int(input())
    s=input()
    i,j=0,n-1
    count=0
    flag=0
    bl,br=0,0
    s=list(s)
    while i<n and j>=0 and i<j :
        if s[i]!=s[j]:
            if i+1==j:
                flag+=1
                print("NO")
                break
            elif br==0 and s[i]==s[j-1]:
                s[j-1],s[j]=s[j],s[j-1]
                count+=1
                bl,br=0,1
            elif bl==0 and s[i+1]==s[j]:
                s[i],s[i+1]=s[i+1],s[i]
                count+=1
                bl,br=1,0
            else:
                flag+=1
                print("NO")
                break    
        else:
            bl,br=0,0      
        i+=1
        j-=1
    if flag==0:    
        print("YES")
        print(count)