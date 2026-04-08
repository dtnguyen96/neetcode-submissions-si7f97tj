from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        s_count = dict(Counter(s))
        t_count = dict(Counter(t))
        return s_count == t_count