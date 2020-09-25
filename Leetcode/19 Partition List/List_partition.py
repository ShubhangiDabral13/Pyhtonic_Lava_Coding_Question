# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:


        beforeval = ListNode(0)
        before = beforeval
        afterval = ListNode(0)
        after = afterval
        while(head):
            if head.val >= x:
                after.next = head
                after = after.next
            else:
                before.next = head
                before = before.next
            head = head.next

        after.next = None
        before.next = afterval.next

        return beforeval.next
