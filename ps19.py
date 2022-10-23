'''Problem statement:
You are given two strings SS and RR. Each of these strings has length NN. We want to make SS equal to RR by performing the following operation some number of times (possibly zero):
Choose two integers aa and bb such that 1 \le a \le b \le N1≤a≤b≤N.
For each ii such that a \le i \le ba≤i≤b, replace the ii-th character of SS by the ii-th character of RR.
Suppose that we make SS equal to RR by performing this operation kk times, in such a way that the total number of replaced characters (i.e. the sum of all kk values of b-a+1b−a+1) is ll. Then, the cost of this process is defined as k \cdot lk⋅l.
Find the minimum cost with which we can make SS equal to RR.

Input
The first line of the input contains a single integer TT denoting the number of test cases. The description of TT test cases follows.
The first line of each test case contains a single string SS.
The second line contains a single string RR.

Output
For each test case, print a single line containing one integer ― the minimum cost.'''

#code

T=int(input())
for i in range(T):
    s=input()
    r=input()
    val=[i for i in range(len(s)) if s[i]!=r[i]]
    a=[val[i+1]-val[i]-1 for i in range(len(val)-1)]
    a.sort()
    k,l=len(val),len(val)
    n=[k*l]
    for i in a:
        k-=1
        l+=i
        n.append(k*l)
    print(min(n))