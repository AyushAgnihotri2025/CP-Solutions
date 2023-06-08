class Solution():
    def maxStop(self, n, m, trains):
        #your code goes here
        platform=[[] for _ in range(m)]
        count=[0 for _ in range(m)]
        trains.sort(key=lambda x:x[1])
        for a,d,p in trains:
            if platform[p-1]==[]:
                platform[p-1]=[a,d]
                count[p-1]+=1
            else:
                if platform[p-1][1]<=a:
                    platform[p-1]=[a,d]
                    count[p-1]+=1
        answer=0
        for i in range(m):
            answer+=count[i]
        return answer

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n,m = map(int, input().split())
        trains = []
        for i in range(m):
            trains.append([int(i) for i in input().split()])
        print(Solution().maxStop(n, m, trains))
# } Driver Code Ends