#User function Template for python3

class Solution:
    def rearrange(self, S, N):
        # code here
        if N == 1:
            return S

        vs = {"a", "e", "i", "o", "u"}

        va = []
        ca = []

        S = sorted(S)

        for ch in S:
            if ch in vs:
                va.append(ch)
            else:
                ca.append(ch)

        if len(va) == len(ca) or len(va) == len(ca) + 1 or len(va) + 1 == len(ca):
            if len(va) < len(ca):
                small = va
                big = ca
            elif len(va) > len(ca):
                small = ca
                big = va
            else:
                if va[0] > ca[0]:
                    big = ca
                    small = va
                else:
                    big = va
                    small = ca

            i = 0
            bi = 0
            si = 0
            new_s = ""

            while i < len(S):
                if i % 2 == 0:
                    new_s += big[bi]
                    bi += 1
                else:
                    new_s += small[si]
                    si += 1

                i += 1

            return new_s
        else:
            return -1

        return ""
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N = int(input().strip())
        S = input().strip()
        ob=Solution()
        ans=ob.rearrange(S, N)
        print(ans)
# } Driver Code Ends