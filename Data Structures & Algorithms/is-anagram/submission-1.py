class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sChar = {}
        tChar = {}
        if len(s) != len(t):
            return False
        else:
            for i in s:
                if i in sChar:
                    sChar[i] += 1
                else:
                    sChar[i] = 1
            
            for i in t:
                if i in tChar:
                    tChar[i] += 1
                else:
                    tChar[i] = 1
            return tChar == sChar
            
        