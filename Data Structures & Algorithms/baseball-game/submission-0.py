class Solution:
    def calPoints(self, operations: List[str]) -> int:
        myArr = []
        num = 0
        for i in operations:
            if i == '+':
                num+=myArr[-2]+myArr[-1]
                myArr.append(myArr[-2]+myArr[-1])
            elif i == 'D':
                num +=myArr[-1]*2
                myArr.append(myArr[-1]*2)
            elif i == 'C':
                num-= myArr[-1]
                myArr.pop()
            else:
                num+= int(i) 
                myArr.append(int(i))
        return num
        
