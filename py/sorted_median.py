"""
Given two sorted arrays nums1 and nums2 of size m and n
respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

from typing import List


def mergeArray(arr1: List[int], arr2: List[int]) -> List[int]:
    i = 0
    j = 0
    res = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    while i < len(arr1):
        res.append(arr1[i])
        i += 1

    while j < len(arr2):
        res.append(arr2[j])
        j += 1

    return res


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    # Brute Force
    mergedArr = mergeArray(nums1, nums2)
    totalLen = len(mergedArr)
    res = 0.0

    if totalLen % 2 != 0:
        res = mergedArr[totalLen // 2]
    else:
        mid1 = mergedArr[totalLen // 2]
        mid2 = mergedArr[totalLen // 2 - 1]
        res = (mid1 + mid2) / 2.0

    return res
