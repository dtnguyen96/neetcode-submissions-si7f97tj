'''
Approach 1: Use hashmap to count occurences of each character, then compared the two hashmap 
Approach 2: Sort the two strings then compare them 

'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        CountS = {}
        CountT = {}
        for i in range(len(s)):
            CountS[s[i]] = 1 + CountS.get(s[i], 0)
            CountT[t[i]] = 1 + CountT.get(t[i], 0)
        for char in s:
            if CountS[char] != CountT.get(char, 0): 
                return False 
        return True