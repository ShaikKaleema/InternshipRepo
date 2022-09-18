# Regular Expression Matching
'''Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
  '.' Matches any single character.​​​​
  '*' Matches zero or more of the preceding element.
  The matching should cover the entire input string (not partial).
e.g. : 
    Input: s = "aa", p = "a*"
    Output: true
    Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        l1=len(s)
        l2=len(p)
        if l1==0 and l2==0:
            return True
        if l2==0:
            return False
        mat=[[False for i in range(l2+1)] for j in range(l1+1)]
        mat[0][0]=True
        for i in range(2,l2+1):
            if p[i-1]=='*':
                mat[0][i]=mat[0][i-2]
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if p[j-1]=='.' or s[i-1]==p[j-1]:
                    mat[i][j]=mat[i-1][j-1]
                elif j>1 and p[j-1]=='*':
                    mat[i][j]=mat[i][j-2]
                    if p[j-2]=="." or p[j-2]==s[i-1]:
                        mat[i][j]=mat[i][j] or mat[i-1][j]
                        
        return mat[l1][l2]
        