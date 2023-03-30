class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def divide(lp, rp):
            if lp < rp:
                mid = (lp+rp)//2
                divide(lp, mid)
                divide(mid+1, rp)
                merge(lp,mid,rp)

        def merge(lp, mid, rp):
            arr1, arr2 = nums[lp:mid+1], nums[mid+1:rp+1]
            i,j,k = 0, 0, lp
            m,n = len(arr1), len(arr2)
            while i < m and j < n:
                if arr1[i] <= arr2[j]:
                    nums[k] = arr1[i]
                    i += 1
                else:
                    nums[k] = arr2[j]
                    j += 1
                k += 1
            nums[k:rp+1] = arr1[i:] if i < m else arr2[j:]
        
        divide(0, len(nums)-1)
        return nums