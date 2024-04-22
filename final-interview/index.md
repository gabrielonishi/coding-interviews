# Final Interview

## H-Index

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

**Example 1:**

> **Input:** `citations = [3,0,6,1,5]`

> **Output:** `3`

> **Explanation:** `[3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.`

> `Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.`

**Example 2:**
**Input:** `citations = [1,3,1]`
**Output:** `1`

**Constraints:**

- `n == citations.length`
- `1 <= n <= 5000`
- `0 <= citations[i] <= 1000`

## Hints

1.  An easy approach is to sort the array first.
2.  What are the possible values of h-index?
3.  A faster approach is to use extra space.

## Solution

### Sorted Solution:

Intuition: if we have the array in descending order, we can iterate over updating the h value. If citations[i] is greater than i, it implies that there are at least i + 1 papers with citations[i] citations each. Therefore, it increments the h-index h by 1.

This approach has a time complexity of $O(n \log n)$ due to the sorting operation. However, it only requires a single pass through the sorted array to determine the h-index, resulting in a relatively efficient solution. Additionally, it has a space complexity of $O(1)$ since it doesn't use any extra space apart from the input array.

**Time Complexity:** $O(nlogn)$
**Space Complexity:** $O(1)$

### Hash Map Solution:

This solution uses a dictionary to store the count of citations for each number of citations. It iterates over the citations array to populate this dictionary. Then, it iterates backward from the maximum citation count to 0 and checks if the cumulative count of papers with citations greater than or equal to the current citation count is greater than or equal to the current citation count. If true, it returns the current citation count as the h-index.

The time complexity is better than the sorted solution because we don't need to sort the array. However, we depend on extra space to compensate.

**Time Complexity:** $O(n)$
**Space Complexity:** $O(n)$

## Reference

[Leetcode 274](https://leetcode.com/problems/h-index/description/)
