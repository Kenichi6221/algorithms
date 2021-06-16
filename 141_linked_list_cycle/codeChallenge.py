# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dumb = ListNode(head)

        if head==None or head.next==None:return False

        dumb.next = head
        tortoise = dumb.next
        hare = tortoise.next

        while tortoise is not hare:
            tortoise = tortoise.next
            if hare.next and hare.next.next:
                hare = hare.next.next
            else:
                return False
        return tortoise is hare