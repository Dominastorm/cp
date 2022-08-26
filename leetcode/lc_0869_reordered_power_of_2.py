class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        x = 1
        for i in range(0, 31):
            if sorted(str(n)) == sorted(str(x)):
                return True
            x *= 2
        return False
    