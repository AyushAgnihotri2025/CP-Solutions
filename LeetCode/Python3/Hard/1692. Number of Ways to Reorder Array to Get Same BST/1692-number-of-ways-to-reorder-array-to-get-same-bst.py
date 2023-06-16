class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 1000000007
        n = len(nums)
        leng = [0]*(n+2)
        cnt = [1]*(n+2)
        for p in nums[::-1]:
            h,k = leng[p-1],leng[p+1]
            t = (cnt[p-1]*cnt[p+1]%mod)*comb(h+k,h)%mod
            leng[p-h]=leng[p+k]=h+k+1
            cnt[p-h]=cnt[p+k]=t
        return (cnt[1]-1)%mod