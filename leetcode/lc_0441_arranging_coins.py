from math import floor, sqrt
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return floor((sqrt(1+8*n)-1)/2)