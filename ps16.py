''' Problem statement :


###Input:
First line will contain TT, number of testcases. Then the testcases follow.
Each testcase contains of a single line of input, a string SS.

###Output: For each testcase, output in a single line "Dynamic" if the given string is dynamic, otherwise print "Not". (Note that the judge is case sensitive)'''

#code

T=int(input())
for i in range(T):
    S=input()
    l1=[]
    #S1=set(s)
    for j in set(S):
        l1=l1+[S.count(j)]
    l1.sort()
    if len(l1)<3:
        print("Dynamic")
    elif (l1[-1]!=l1[-2]+l1[-3]):
        print("Not")
    else:
        print("Dynamic")