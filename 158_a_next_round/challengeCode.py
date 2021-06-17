import sys
from typing import List

class Solution:
  def next_round(self,minimum_approved:int, constestant_scores:List[int])->int:
    size = len(constestant_scores)

    approved = 0
    minimum_value = 1
    for pos in range(size):
      if constestant_scores[pos]>=minimum_value:approved+=1
      if minimum_value == 1 and approved == minimum_approved: minimum_value=constestant_scores[pos]

    return approved