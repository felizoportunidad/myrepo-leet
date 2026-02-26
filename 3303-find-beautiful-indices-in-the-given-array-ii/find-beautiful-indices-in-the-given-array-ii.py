class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        
        a_pos = [i for i in range(len(s)) if s.startswith(a, i)]
        b_pos = [i for i in range(len(s)) if s.startswith(b, i)]

        i = j = 0
        n = len(a_pos)
        m = len(b_pos)

        res = []
        
        while i < n and j < m:

            if abs(a_pos[i] - b_pos[j]) <= k:
                res.append(a_pos[i])
                i += 1
            elif a_pos[i] < b_pos[j]-k:
                i += 1
            elif b_pos[j] < a_pos[i]-k:
                j+=1
            
        return res