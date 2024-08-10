/**
 *Given an integer array nums and an integer k, return the k most frequent
elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n),
where n is the array's size.
 */

class Solution {
public:
  vector<int> topKFrequent(vector<int> &nums, int k) {
    std::vector<int> result;
    std::unordered_map<int, int> counts;

    for (int n : nums) {
      counts[n]++;
    }

    // Using Max-Heap structure
    typedef pair<int, int> heap_node;
    std::priority_queue<heap_node, vector<heap_node>, std::greater<heap_node>>
        max_heap;

    // Pushing each element {number : frequency} into heap
    for (auto &c : counts) {
      max_heap.push({c.second, c.first});

      // When heap size becomes greater than k, the smallest count is
      // popped
      if (max_heap.size() > k)
        max_heap.pop();
    }

    while (!max_heap.empty()) {
      // The top element of the heap (highest freq)
      pair<int, int> top_count = max_heap.top();
      result.push_back(top_count.second);

      // Popping the top element to get the next highest element
      max_heap.pop();
    }

    return result;
  }
};
