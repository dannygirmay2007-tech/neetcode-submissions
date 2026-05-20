class Solution:
    def isValid(self, s: str) -> bool:
        current = []
        for st in s:
            if st == "(" or st == "[" or st == "{":
                current.append(st)
            elif len(current) >= 1 and st == ")" and current[-1] == "(":
                del current[-1]
            elif len(current) >= 1 and st == "]" and current[-1] == "[":
                del current[-1]
            elif len(current) >= 1 and st == "}" and current[-1] == "{":
                del current[-1]
            else:
                return False
        if len(current) != 0:
            return False
        return True
                