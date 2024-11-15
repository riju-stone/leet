/**
 * Given two strings s and t, return true if t is an anagram of s, and false
otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt
your solution to such a case?
 */

class Solution {
public:
  bool isAnagram(string s, string t) {

    // If both strings are not equal in length
    if (s.size() != t.size()) {
      return false;
    }

    std::unordered_map<char, int> count_map;
    // Count the frequency of each character in s
    for (const char c : s) {
      count_map[c]++;
    }

    /**
        Reduce count every time a known character is encountered in t.
        If any unknown character is encountered return false.
    */
    for (const char c : t) {
      if (count_map.find(c) == count_map.end())
        return false;

      count_map[c]--;
    }

    // Check if any character has count greater than 0
    for (const auto &val : count_map) {
      if (val.second != 0)
        return false;
    }

    return true;
  }
};
