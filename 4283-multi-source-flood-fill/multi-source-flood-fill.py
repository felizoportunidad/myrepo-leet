class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        d = [[0 for _ in range(m)] for _ in range(n)]

        q = deque()
        sources.sort(key = lambda x: -x[2])

        for i,j,c in sources:
            q.append((i,j,c))
            d[i][j] = c


        while q:
            curi,curj,curcolor = q.popleft()
            for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]:
                ni = curi + di
                nj = curj + dj
                if ni < 0 or ni >= n:
                    continue
                if nj < 0 or nj >= m:
                    continue
                if d[ni][nj] != 0:
                    continue
                d[ni][nj] = curcolor
                q.append((ni,nj,curcolor))

        return d
