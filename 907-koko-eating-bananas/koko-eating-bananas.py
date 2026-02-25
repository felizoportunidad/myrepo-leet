class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isPossible(k):
            time = 0
            for e in piles:
                time += math.ceil(e / k)
                
            return time <= h

        left = 1
        right = max(piles)
        ans = right
        while left <= right:
            mid = (left + right) // 2

            if isPossible(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans