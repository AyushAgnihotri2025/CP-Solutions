#User function Template for python3

class Solution:
    def printUniqueSubset(self, nums):
        # Code here
        nums.sort()
        def powerSet(nums,index,curr,ans):
            if index==len(nums):
                ans.append(curr)
                return
            else:
                powerSet(nums,index+1,curr,ans)
                powerSet(nums,index+1,curr+[nums[index]],ans)
        ans=[]
        curr=[]
        index=0
        powerSet(nums,index,curr,ans)
        ans.sort()
        unique_set = set()
        for sublist in ans:
            sublist_tuple = tuple(sublist)
            unique_set.add(sublist_tuple)
        unique_list = [list(t) for t in unique_set]
        unique_list.sort()
        return (unique_list)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        nums = list(map(int, input().split()))
        ob = Solution()
        res = ob.printUniqueSubset(nums)
        print('[ ', end = '')
        for subset in res:
            print('[ ', end = '')
            for val in subset:
                print(val, end = ' ')
            print(']', end = '')
        print(' ]')
# } Driver Code Ends