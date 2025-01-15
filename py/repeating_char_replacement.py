"""
You are given a string s and an integer k. You can choose any character of the
string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get
after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

Constraints:
1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""


def characterReplacement(s: str, k: int) -> int:
    left = 0
    freq = {}
    longest_count = 0

    for right in range(len(s)):
        if s[right] not in freq:
            freq[s[right]] = 0
        freq[s[right]] += 1

        window_len = right - left + 1
        if window_len - max(freq.values()) <= k:
            longest_count = max(longest_count, window_len)
        else:
            if freq[s[left]] > 0:
                freq[s[left]] -= 1
            left += 1
    return longest_count


if __name__ == "__main__":
    res = characterReplacement("ABAB", 2)
    print(res)
