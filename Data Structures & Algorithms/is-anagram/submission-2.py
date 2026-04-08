from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        s_count = dict(Counter(s))
        t_count = dict(Counter(t))
        for k,v in s_count.items():
            if k not in t_count:
                return False
            elif t_count[k] != v:
                return False 
        return True