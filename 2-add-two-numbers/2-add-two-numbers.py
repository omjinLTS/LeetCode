# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def getNum(l: Optional[ListNode]):
    ret = ''
    while l.next != None:
        ret += str(l.val)
        l = l.next
    ret += str(l.val)
    return int(ret[::-1])
            

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = str(getNum(l1) + getNum(l2))
        ret = ListNode(res[-1])
        for n in res[:-1]:
            nxt = ListNode(n, ret.next)
            ret.next = nxt
        return ret
            
        
            