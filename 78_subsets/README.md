# Description:

![challenge image from: leetcode.com](challenge.png)

The above image description regarded to this challege was taked from

[leetcode:78. Subsets](https://leetcode.com/problems/subsets/)

## Approach I: Backtrack

Here, we can use a backtrack solution with next structure:

- candidates: [include_kth_element,not_include_kth_element]
- base case: len(subset) == len(original_array)
- Each subset (finished) will be added to final_solution array

## Final Result

![final result: leetcode.com](Summary_Approach_I.png)

**Related topics**: Backtracking, [Powerset](https://en.wikipedia.org/wiki/Power_set)
