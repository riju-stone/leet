/**
 * Given an integer array nums, return true if any value appears at least twice
in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
 */
#include "unordered_map"
#include "vector"

using namespace std;

class Solution {
public:
  bool containsDuplicate(vector<int> &nums) {
    vector<int>::iterator itr;

    // Using Unordered Set
    // std::unordered_set<int> set;
    // for(itr = nums.begin(); itr != nums.end(); itr++){
    //     if(set.count(*itr) > 0)
    //         return true;
    //     set.insert(*itr);
    // }

    // return false;

    // Using Unordered Map
    std::unordered_map<int, int> map;
    for (itr = nums.begin(); itr != nums.end(); itr++) {
      if (map[*itr] >= 1)
        return true;
      else
        map[*itr]++;
    }

    return false;
  }
};
