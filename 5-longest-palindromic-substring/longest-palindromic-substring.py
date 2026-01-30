class Solution:
    def longestPalindrome(self, s: str) -> str:    
        n = len(s)
        
        if n <=1:
            return s
        
        dp = [[False]*n for _ in range(n)]
        
        ans = ''
        maxlen = 1
        
        for i in range(n):
            dp[i][i]=True
            ans = s[i:i+1]
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1]=True
                ans = s[i:i+2]
                maxlen = 2
                
        for j in range(n):
            for i in range(j-1):
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j]=True
                    if j-i+1 > maxlen:
                        maxlen = j - i + 1
                        ans = s[i:j+1]
                        
        return ans
