#Roman to Integer conversion
class Solution:
    def romanToInt(self, s: str) -> int:
        dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        n=len(s)
        res=dict[s[n-1]]
        for i in range(n-2,-1,-1):
            if dict[s[i]] >= dict[s[i+1]] :
                res=res+dict[s[i]]
            else:
                res=res-dict[s[i]]
        return res
    
    
#Use Same List Of Items In This Problem as Well Pls Refer to https://github.com/ShaikKaleema/InternshipRepo/pull/1/commits/09b9e97629b64ae76cf94089405394fd5fead9ff    
