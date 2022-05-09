# take number of test cases as input
T = int(input())

# loop through test cases
for i in range(T):
    # take input - 8 lines
    tr = int(input())
    Tr = set(map(int, input().split()))
    dr = int(input())
    Dr = set(map(int, input().split()))
    ts = int(input())
    Ts = set(map(int, input().split()))
    ds = int(input())
    Ds = set(map(int, input().split()))

    res = list(Ts-Tr)+list(Ds-Dr)
    if res == []:
        print('yes')
    else:
        print('no')