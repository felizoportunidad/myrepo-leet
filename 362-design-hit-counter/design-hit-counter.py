from collections import deque
from bisect import bisect_left

class HitCounter:

    def __init__(self):
        self.q = []

    def hit(self, timestamp: int) -> None:
        self.q.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        i = bisect_left(self.q,timestamp-300+1)
        return len(self.q)-i



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)