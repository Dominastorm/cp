class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        l = len(seats)
        # only one occupied seat
        if seats.count(1) == 1:
            # occupied seat is on the left side
            pos = seats.index(1)
            if pos < (l-1)/2:
                return l - pos - 1
            # occupied seat is on the right side or in the middle
            else:
                return pos
        # if multiple seats are occupied
        else:
            maxDist = seats.index(1)
            print(seats)
            i = 0
            while i < l and 1 in seats[i:]:
                if seats[i] == 1 and 1 in seats[i+1:]:
                    dist = seats[i+1:].index(1) + 1
                    i += dist
                    if dist//2 > maxDist:
                        maxDist = dist//2
                else:
                    i += 1
            if seats[-1] == 0:
                maxDist = max(seats[::-1].index(1), maxDist)
                
            return maxDist