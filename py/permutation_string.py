"""
Given two strings s1 and s2, return true if s2 contains a permutation
of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""


def checkInclusion(s1: str, s2: str) -> bool:
    # Hash Map Solution
    # s1count = {}

    # for i in range(len(s1)):
    #     if s1[i] not in s1count:
    #         s1count[s1[i]] = 0
    #     s1count[s1[i]] += 1

    # window_size = len(s1)
    # for i in range(len(s2)):
    #     s2count = {}
    #     matches = 0

    #     for j in range(i, len(s2)):
    #         if s2[j] not in s2count:
    #             s2count[s2[j]] = 0
    #         s2count[s2[j]] += 1

    #         if s1count.get(s2[j], 0) < s2count[s2[j]]:
    #             break
    #         if s1count.get(s2[j], 0) == s2count[s2[j]]:
    #             matches += 1
    #         if window_size == matches:
    #             return True

    # Sliding Window Solution
    s1_count = [0] * 26
    s2_count = [0] * 26

    if len(s2) < len(s1):
        return False

    for i in range(len(s1)):
        s1_count[ord(s1[i]) - ord("a")] += 1
        s2_count[ord(s2[i]) - ord("a")] += 1

    if s1_count == s2_count:
        return True

    left = 0
    for right in range(len(s1), len(s2)):
        # reduce the count of the leftmost character that was pushed out of the window
        left_idx = ord(s2[left]) - ord("a")
        s2_count[left_idx] -= 1

        # increase the count of the rightmost character that was pushed in the window
        right_idx = ord(s2[right]) - ord("a")
        s2_count[right_idx] += 1

        if s1_count == s2_count:
            return True

        left += 1

    return False


if __name__ == "__main__":
    res = checkInclusion("ab", "erftwfba")
    print(res)
