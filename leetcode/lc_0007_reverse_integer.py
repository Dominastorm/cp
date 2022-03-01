class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x == '0':
            return 0
        elif x[0] == '-':
            x = int('-' + x[1:].rstrip('0')[::-1])
        else:
            x = int(x.rstrip('0')[::-1])
        if x < -2**31 or x > 2**31 -1:
            return 0
        return x