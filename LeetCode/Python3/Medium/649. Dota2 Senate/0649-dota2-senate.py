class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queues = [deque(), deque()]
        for i, c in enumerate(senate):
            queues[int(c == 'R')].append(i)
        while queues[0] and queues[1]:
            r, c = queues[1].popleft(), queues[0].popleft()
            queues[int(r < c)].append((r if r < c else c) + len(senate))
        return 'Radiant' if queues[1] else 'Dire'