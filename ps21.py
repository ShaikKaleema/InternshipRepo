'''Problem statement :
In this problem you will have to implement a simple editor. The editor maintains the content of a string S and have two following functions:
"+ i x": insert a string x into the current string S after the i'th character of the S (we use 1-indexing in this problem). When i equals to 0 it mean we add x at the beginning of S.
"? i len": Print the sub-string of length len starting at position i'th of S.
At the beginning, the editor holds an empty string. There will be Q queries of the two types described above.

Input
The first line contains the integer Q. Each line in the next Q lines contains one query.

Output
For each query of the second type, print out the answer sub-string in one line.'''

#code 

n=int(input())
s=""
for i in range(n):
    x=input().split()
    if x[0]=='+':
        s=s[:int(x[1])]+x[2]+s[int(x[1]):]
    else:
        print(s[(int(x[1])-1):((int(x[2])+int(x[1])-1))])