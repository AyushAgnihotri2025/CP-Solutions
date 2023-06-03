class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ans=[]
        for lv,level in enumerate(triangle):
            mins=[]
            if lv == 0:
                mins.append(level[0])
            else: 
                for i, n in enumerate(level):
                    if i == 0:
                        mins.append(ans[lv-1][i]+n)
                    elif i == len(level)-1:
                        mins.append(ans[lv-1][i-1]+n)
                    else:
                        mins.append(min(ans[lv-1][i],ans[lv-1][i-1])+n)
            ans.append(mins)
        return min(ans[-1])