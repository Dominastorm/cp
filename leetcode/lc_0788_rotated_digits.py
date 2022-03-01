class Solution:
    def validNumber(self, d, n:int) -> int:
        s = [int(i) for i in str(n)]
        for i in range(len(s)):
            if s[i] in d:
                s[i] = d[s[i]]
            else:
                return 0
        return int("".join([str(i) for i in s])) != n                     
        
    def rotatedDigits(self, n: int) -> int:
        count = 0
        d = {0:0, 1:1, 2:5, 5:2, 6:9, 8:8, 9:6}
        for i in range(1, n+1):
            if Solution().validNumber(d, i):
                count += 1
        return count