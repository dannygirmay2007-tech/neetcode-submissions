class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        dic2 = {}
        for sr in s:
            dic[sr] = dic.get(sr, 0) +1
        for sr in t:
            dic2[sr] = dic2.get(sr, 0) +1  
        return dic == dic2