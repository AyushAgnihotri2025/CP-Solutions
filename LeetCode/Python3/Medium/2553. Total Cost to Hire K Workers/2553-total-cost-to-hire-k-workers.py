import heapq
import math
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        leftHeap = []
        for i in range(0, min(candidates, len(costs))):
            leftHeap.append((costs[i], i))
        heapq.heapify(leftHeap)
        max_left_index = candidates-1
        rightHeap = []
        min_right_index = max(len(costs)-candidates, max_left_index+1)
        for i in range(min_right_index, len(costs)):
            rightHeap.append((costs[i], i))
        heapq.heapify(rightHeap)
        total = 0
        for _ in range(k):
            leftCandidate = leftHeap[0] if leftHeap else (math.inf, math.inf)
            rightCandidate = rightHeap[0] if rightHeap else (math.inf, math.inf)
            if (leftCandidate < rightCandidate):
                heapq.heappop(leftHeap)
                total += leftCandidate[0]
                max_left_index += 1
                if max_left_index < min_right_index:
                    heapq.heappush(leftHeap, (costs[max_left_index], max_left_index))
            else:
                heapq.heappop(rightHeap)
                total += rightCandidate[0]
                min_right_index -= 1
                if min_right_index > max_left_index:
                    heapq.heappush(rightHeap, (costs[min_right_index], min_right_index))
        return total