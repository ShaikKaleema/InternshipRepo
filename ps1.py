'''Problem : sleep deprivation
A person is said to be sleep deprived if he slept strictly less than 77 hours in a day.
Chef was only able to sleep XX hours yesterday. Determine if he is sleep deprived or not.
Input Format :
The first line contains a single integer TT — the number of test cases. Then the test cases follow.
The first and only line of each test case contains one integer XX — the number of hours Chef slept.
Output Format :
For each test case, output YES if Chef is sleep-deprived. Otherwise, output NO.
You may print each character of YES and NO in uppercase or lowercase (for example, yes, yEs, Yes will be considered identical).'''
# Code :
T=int(input())
l=[]
for i in range(T):
    k=int(input())
    l.append(k)
for j in range(T):
    if l[j]<7:
        print('YES')
    else:
        print('NO')
            
