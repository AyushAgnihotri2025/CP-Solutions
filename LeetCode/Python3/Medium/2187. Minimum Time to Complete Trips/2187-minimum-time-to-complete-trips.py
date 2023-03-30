class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        n = len(time)
        l = 0
        r = max(time) * totalTrips
        while l < r:
            mid = (l + r) // 2
            trips = 0
            for i in range(n):
                trips += mid // time[i]
            if trips >= totalTrips:
                r = mid
            else:
                l = mid + 1
        return l