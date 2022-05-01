class Solution:        
    def backspaceCompare(self, s: str, t: str) -> bool:
        def replace(s):
            s = s[::-1]
            res = []
            count = 0
            for i in range(len(s)):
                if s[i] == '#':
                    count += 1
                elif count:
                    count -= 1
                else:                    
                    res += s[i]
            return res
        s, t = replace(s), replace(t)
        print(s, t)
        return s == t

if __name__ == "__main__":
    s = Solution()
    print(s.backspaceCompare("ab#c", "ad#c"))
    print(s.backspaceCompare("ab##", "c#d#"))
    print(s.backspaceCompare("a##c", "#a#c"))
    print(s.backspaceCompare("a#c", "b"))