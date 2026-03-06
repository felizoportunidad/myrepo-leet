class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        rows = len(costs)
        if rows == 0: return 0
        cols = len(costs[0])
        if cols == 0: return 0

        dp = [[float('inf')]*cols for _ in range(rows)]

        dp[0] = costs[0]
        
        for i in range(1,rows):
            for j in range(0,cols):
                for k in range(0,cols):
                    if k == j:
                        continue
                    else:
                        dp[i][j] = min(dp[i-1][k]+costs[i][j], dp[i][j])

        return min(dp[rows-1][c] for c in range(cols))