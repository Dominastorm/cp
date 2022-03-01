n = int(input())
l = []
seq = set()
for i in range(n):
    inp = tuple(input().split(" "))
    seq.add(inp)
print(len(seq))        