''' Problem statement :
Given a binary string SS consisting of 0's0 
′
 s and 1's1 
′
 s, find whether there exists a rightwise circular rotation of the string such that every 2 adjacent 1's1 
′
 s are separated by at most CC 0's0 
′
 s.

Note: The last occurrence of 11 in the rotated string won't have any 11 next to it, i.e, first and the last ones in the string are not considered to be adjacent.

###Input:
First line will contain TT, number of testcases. Then the testcases follow.
Each testcase contains of two lines of input.
First line contains two space separated integers N, CN,C, length of the string and the upper limit on a number of 0's0 
′
 s between 22 adjacent 1's1 
′
 s.
Second line contains the binary string SS.

###Output: For each testcase, output in a single line "YES" if there exists a rightwise circular rotation of string satisfying the criteria and "NO" if it doesn't exist.'''

#code

T=int(input())
for i in range(T):
    n,c=map(int,input().split())
    s=input()
    s1=s.split('1')
    l1=[]
    if s.count('1')==0 or s.count('1')==1:
        print('YES')
    else:
        for i in s1:
            l1.append(len(i))
        if s[0]=='0' and s[-1]=='0':
            l1[0]=l1[-1]+l1[0]
            l1.pop()
        l1.sort()
        l1.pop()
        if c<max(l1):
            print('NO')
        else:
            print('YES')