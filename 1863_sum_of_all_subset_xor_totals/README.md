# Description:

![challenge image from: leetcode.com](challenge.png)

The above image description regarded to this challege was taked from

[leetcode:1863. Sum of All Subset XOR Totals](https://leetcode.com/problems/sum-of-all-subset-xor-totals/)

## Aproach I: backtracking

Here, I will use a backtracking approach as follow:

- Stop: Kth element evaluated (added or not) == len(original_subset)
- Possible decisions each iteration: [include_kth, not_include_kth]

When I had created a new subset

- if len(subset) > 0 :
  - Apply XOR with each element
  - Add totalized element to totalized_array in position 0

After above operations: result = totalized_array[0]

## Final Result

![final result: {challenge page}.com](summary_approach_I.png)

**Related topics**: backtracking, [Powersets](https://en.wikipedia.org/wiki/Power_set)
