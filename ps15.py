'''
Problem statement :A sequence of integers is beautiful if each element of this sequence is divisible by 4.
You are given a sequence a1, a2, ..., an. In one step, you may choose any two elements of this sequence, remove them from the sequence and append their sum to the sequence. Compute the minimum number of steps necessary to make the given sequence beautiful.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer n.
The second line contains n space-separated integers a1, a2, ..., an.
Output
For each test case, print a single line containing one number — the minimum number of steps necessary to make the given sequence beautiful. If it's impossible to make the sequence beautiful, print -1 instead.'''

#code

T=int(input())
for i in range(T):
    n=int(input())
    A=list(map(int,input().split()))
    for i in range(n):
        A[i]=A[i]%4
    if sum(A)%4:
        print(-1)
        continue
    a1,a2,a3=A.count(1),A.count(2),A.count(3)
    p,q=max(a1,a3),min(a1,a3)
    p=p-q
    res=q+(p//4)*3+(p%4)+a2//2
    print(res)