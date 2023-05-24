class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i=0
        intervals.sort()
        if len(intervals)==0:
            return []
        elif len(intervals)==1:
            return list(intervals)
        else:
            while i<len(intervals)-1:
                if(intervals[i][1]>=intervals[i+1][0] and intervals[i][1]>=intervals[i+1][1]):
                    intervals.append([intervals[i][0],intervals[i][1]])
                    intervals.remove(intervals[i])
                    intervals.remove(intervals[i])
                    intervals.sort()

                elif(intervals[i][1]>=intervals[i+1][0] and intervals[i][1]<intervals[i+1][1]):
                    intervals.append([intervals[i][0],intervals[i+1][1]])
                    intervals.remove(intervals[i])
                    intervals.remove(intervals[i])
                    intervals.sort()
                else:
                    i+=1
            return intervals