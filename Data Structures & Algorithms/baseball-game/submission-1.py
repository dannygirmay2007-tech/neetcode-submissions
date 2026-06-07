class Solution:
    def calPoints(self, operations: List[str]) -> int:
        myArr = []
        for i in operations:
            if i == '+':
                myArr.append(myArr[-2]+myArr[-1])
            elif i == 'D':
                myArr.append(myArr[-1]*2)
            elif i == 'C':
                myArr.pop()
            else:
                myArr.append(int(i))
        return sum(myArr)
        
