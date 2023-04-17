#User function Template for python3

class Solution:
    
    #Function to find the maximum profit and the number of Jobs done.
    def JobScheduling(self,Jobs,n):
        
        # code here
        Jobs.sort(key=lambda j: -j.profit)
        max_deadline = max(Jobs, key=lambda j: j.deadline).deadline
        
        slots = [False]*(max_deadline+1)
        profit, n = 0, 0
        for job in Jobs:
            for k in range(job.deadline, 0, -1):
                if not slots[k]:
                    slots[k] = True
                    profit += job.profit
                    n += 1
                    break
        return n, profit


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        ob = Solution()
        res = ob.JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])
# } Driver Code Ends