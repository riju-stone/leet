"""
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have
to wait after the ith day to get a warmer temperature. If there is no
future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""

from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    # brute method
    arr_len = len(temperatures)
    count = [0] * len(temperatures)

    # for i in range(0, arr_len):
    #     for j in range(i, arr_len):
    #         if temperatures[j] > temperatures[i]:
    #             count[i] = j - i
    #             break

    # optimized method
    stack = []
    for i in range(0, arr_len):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            idx = stack.pop()
            count[idx] = i - idx
        stack.append(i)

    return count


if __name__ == "__main__":
    res = dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])

    print(f"Result: {res}")
