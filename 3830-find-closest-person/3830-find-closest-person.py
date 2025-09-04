import math
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        xdist=abs(x-z)
        ydist=abs(y-z)
        if xdist<ydist:
            return 1
        elif xdist>ydist:
            return 2
        else:
            return 0

        