class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = {}
        included = 0
        for i in t:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        mini_len = float("inf")
        ans = ""
        i = 0
        j = 0
        while j<len(s) and s[j] not in d:
            j+=1
            i+=1 
        if j == len(s):
            return ""
        while j<len(s):
            if s[j] in d:
                if d[s[j]] > 0:
                    included += 1
                d[s[j]]-=1
                
            while included == len(t) and i<=j:
                if mini_len > j-i+1:
                    mini_len = j-i+1
                    ans = s[i:j+1]
                if s[i] in d:
                    d[s[i]] += 1
                    if d[s[i]] > 0:
                        included-=1
                i+=1
            
            j+=1
        return  ans
            
            
            