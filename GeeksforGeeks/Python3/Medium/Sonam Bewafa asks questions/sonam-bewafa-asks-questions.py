#User function Template for python3

class Solution:
    def getTestMarks(self, n, q, r, l, rank, storeAnswer):
        # every array is 1-indexed
        score = []
        for i in range(1, n+1):
            score.append((l[i], r[i]))
        score.sort()
        cnt = []
        for i in range(n):
            curr = score[i][1] - score[i][0] + 1
            if i == 0:
                cnt.append(curr)
            else:
                cnt.append(cnt[i-1] + curr)
        for i in range(1, q+1):
            lo, hi = 0, n-1
            ans = -1
            while lo <= hi:
                mi = (lo + hi) // 2
                if cnt[mi] >= rank[i]:
                    ans = mi
                    hi = mi - 1
                else:
                    lo = mi + 1
            if ans == -1:
                storeAnswer[i] = score[n-1][1] + rank[i] - cnt[n-1]
            else:
                before = cnt[ans-1] if ans > 0 else 0
                storeAnswer[i] = rank[i] - before + score[ans][0] - 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, q = sz[0], sz[1]
        l = [0]*(n+5)
        r = [0]*(n+5)
        rank = [0]*(q+5)
        storeAnswer = [0]*(q+5)
        
        st = [int(x) for x in input().strip().split()]
        for i in range(0, 2*n, 2):
            l[(i//2) + 1] = st[i]
            r[(i//2) + 1] = st[i+1]
            
        a = [int(x) for x in input().strip().split()]
        for i in range(q):
            rank[i + 1] = a[i]
        ob=Solution()
        ob.getTestMarks(n, q, r, l, rank, storeAnswer)
        
        output = ''
        for i in range(1,q+1):
            output += str(storeAnswer[i])
            output += ' '
            
        print(output)

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends