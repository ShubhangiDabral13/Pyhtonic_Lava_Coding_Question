# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        c = set()
        while headA != None:
            c.add(headA)
            headA = headA.next

        while headB != None:
            if headB in c:
                return headB
            headB = headB.next
