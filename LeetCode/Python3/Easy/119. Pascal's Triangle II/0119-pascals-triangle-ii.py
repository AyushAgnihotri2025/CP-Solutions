class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        new_list=[1,1]
        old_list=[1]
        if rowIndex==0:
            return old_list
        if rowIndex==1:
            return new_list
        for i in range(2,rowIndex+1):
            old_list = new_list
            new_list=[1]
            for j in range(1,i):
                new_list.append(old_list[j-1]+old_list[j])
            new_list.append(1)
        return new_list