'''Problem statement :
Special Sum of 4 numbers (a, b, c, d) is defined as:
|a+b-c-d| + |a+c-b-d| + |a+d-b-c| + |c+d-a-b| + |b+d-a-c| + |b+c-a-d|
where |x| denotes absolute value of x.
Given an array A of size N, you need to find the sum of Special Sum of numbers taken over all quadruples of different indices of the array.

Input
First line contains T, the number of test cases to follow.
First line of each test case contains the only integer N.
Second line of each test case contains the array as N space separated integers.

Output
For each test case output the sum as explained above.'''

#code

def fun(a,n):
    s = 0
    for i in range(n):
        s += a[i]*(i-(n-i-1))
    return s*2
T=int(input())       
for i in range(T):
    n = int(input())
    a = sorted(list(map(int,input().split())))
    b = []
    for i in range(n-1):
        for j in range(i+1,n):
            b.append(a[i]+a[j])
    b.sort()
    e = fun(b,len(b))
    f = fun(a,n)
    g = e-f*(n-2)
    print(g)