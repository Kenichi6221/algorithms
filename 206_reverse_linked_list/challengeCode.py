## only to in local windows test
import os
import sys

from typing import List
current_folder = os.path.dirname(os.path.realpath(__file__))
# redirect input from input.txt file
sys.stdin = open("{}\\input.txt".format(current_folder), "r")

# redirect output tou output.txt file
sys.stdout = open('{}\\output.txt'.format(current_folder), 'w')
##

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# code solution
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        aux_head = ListNode(next=head)
        prev = aux_head
        curr = aux_head.next

        while curr and curr.next:
            next = curr.next
            curr.next = next.next
            next.next = prev.next
            prev.next = next

        return aux_head.next

#  only local tests
if __name__ == '__main__':
    sol = Solution()
    for line in sys.stdin:
      collection = [int(element) for element in line.split(",")]
      root = ListNode()
      if len(collection)>0:
        root.val = collection[0]
        head = root
        for node in range(1,len(collection)):
          head.next=ListNode(val=collection[node])
          head= head.next
      result = sol.reverseList(root)
      while result:
        print(result.val,end="")
        result= result.next
      print("")
