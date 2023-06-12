class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        list1 = set()
        list2 = set()
        l = len(s)
        if l<=10:
            return list(list1)
        for i in range(0, l-9):
            stri = s[i:i+10]
            if stri in list1 and stri not in list2:
                list2.add(stri)
            elif stri not in list1:
                list1.add(stri)
        return list(list2)