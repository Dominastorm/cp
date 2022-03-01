class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        str2int = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        int2str = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
        num1 = sum([str2int[num1[i]]*10**(len(num1)-i-1) for i in range(len(num1))])
        num2 = sum([str2int[num2[i]]*10**(len(num2)-i-1) for i in range(len(num2))])
        prod = num1*num2
        if prod == 0:
            return "0"
        res = ""
        i = 0
        while prod:
            res += int2str[prod - (prod//10)*10]
            prod //= 10
        return res[::-1]