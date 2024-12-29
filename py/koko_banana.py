from typing import List


def getTimeRequiredToEat(piles, speed):
    hours = 0
    for pile in piles:
        hours += pile // speed
        if pile % speed != 0:
            hours += 1

    return hours


def minEatingSpeed(piles: List[int], h: int):
    low = 1
    high = max(piles)

    while low <= high:
        mid = (low + high) // 2

        if getTimeRequiredToEat(piles, mid) <= h:
            high = mid - 1
        else:
            low = mid + 1

    return low


if __name__ == "__main__":
    res = minEatingSpeed([3, 6, 7, 11], 8)
    print(res)
