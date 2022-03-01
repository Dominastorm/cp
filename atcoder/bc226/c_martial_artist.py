n = int(input())

moves = {}
for i in range(1, n+1):
    inp = tuple([int(i) for i in input().split(" ")])
    moves[i] = inp

toLearn = {i for i in moves[n][2:]}
learnt = set()
time = moves[n][0]

for i in toLearn:
    if i not in learnt:
        time += moves[i][0]
        learnt.add(i)
        toLearn |= {i for i in moves[i][2:]} 

print(time)