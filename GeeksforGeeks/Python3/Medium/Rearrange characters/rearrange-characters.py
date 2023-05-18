#User function Template for python3
from collections import *
import heapq

class Solution :
    def rearrangeString(self, str):
        #code here
        dic=Counter(str)
        heap=[[-count,char] for char,count in dic.items()]
        heapq.heapify(heap)
        output=""
        prev=None
        while heap or prev:
            if prev and not heap:
                return ""
            count,char=heapq.heappop(heap)
            count+=1
            output+=char
            if prev:
                heapq.heappush(heap,prev)
                prev=None
            if count!=0:
                prev=[count,char]
        return output


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        str1 = input()
        solObj = Solution()
        str2 = solObj.rearrangeString(str1)
        if str2=='-1':
            print(0)
        elif sorted(str1)!=sorted(str2):
            print(0)
        else:
            for i in range(len(str2)-1):
                if str2[i]==str2[i+1]:
                    print(0)
                    break
            else:
                print(1)
        
# } Driver Code Ends