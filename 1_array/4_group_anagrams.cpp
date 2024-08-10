/**
 *Given an array of strings strs, group the anagrams together. You can return
the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
 */

class Solution {
private:
  std::string generateWordKey(std::string word) {
    std::string word_key;
    vector<int> counts(26);

    for (int i = 0; i < word.size(); i++) {
      int index = word[i] - 'a';
      counts[index]++;
    }

    for (int j = 0; j < counts.size(); j++) {
      word_key.append(to_string(counts[j]) + "/");
    }

    return word_key;
  }

public:
  vector<vector<string>> groupAnagrams(vector<string> &strs) {
    vector<vector<std::string>> result;
    unordered_map<std::string, vector<std::string>> word_groups;

    for (const std::string &str : strs) {
      std::string word = str;

      // Solution 1: Sorting the characters in the word
      // std::sort(word.begin(), word.end());

      // Solution 2: Creating a custom hash function
      std::string word_key = generateWordKey(str);

      // Grouping similar words based on similar hash key

      // Solution 1:
      // word_groups[word].push_back(str);

      // Solution 2:
      word_groups[word_key].push_back(str);
    }

    // Storing the final map data in vector format
    for (auto &group : word_groups) {
      result.push_back(group.second);
    }

    return result;
  }
};
