class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (2**31) % n == 0
        