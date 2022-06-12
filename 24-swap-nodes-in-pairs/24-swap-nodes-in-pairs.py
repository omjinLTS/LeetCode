# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return
        second = head.next
        if second == None: return head
        third = second.next
        second.next = head
        head.next = self.swapPairs(third)
        return second