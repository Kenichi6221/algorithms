# Description:

![challenge image from: leetcode.com](challenge.png)

The above image description regarded to this challege was taked from

[leetcode:287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)

## Analysis:

Here, is important take the next sentence in mind "All integers in nums appear only once except for precisely one integer that appears two or more times," so the repeated number is only one, then sorting the array can be useful to find the repeated number.

We will sort the array in place swapping each value position to its correct position and checking visited values with a dictionary.

### Cornercases:

- nums.length = 2
- duplicate number in last position
- duplicate number in first position
- duplicate number in middle position
- nums.length is odd
- nums.length is even
- all numbers are the same

## Approach:

- Sort array swping in place
- Use a dictionary to save visited numbers

## Final Result

![final result: leetcode.com](summary_image.png)

**Related topics**:Array, Two pointers
