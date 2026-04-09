class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        @lru_cache(None)
        def dp(i,j,k):
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            
            if k == len(s3):
                return False

            ans = False

            if i < len(s1) and s3[k]==s1[i]:
                ans |= dp(i+1,j,k+1)

            if j < len(s2) and s3[k]==s2[j]:
                ans |= dp(i,j+1,k+1)
            
            return ans

        return dp(0,0,0)