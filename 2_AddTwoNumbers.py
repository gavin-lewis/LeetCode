# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode],carry=0) -> Optional[ListNode]:
        sum=l1.val+l2.val+carry
        carry=sum//10
        ret=ListNode(sum%10)
        if l1.next!=None or l2.next!=None or carry!=0:
            if l1.next==None:
                l1.next=ListNode()
            if l2.next==None:
                l2.next=ListNode()
            ret.next=self.addTwoNumbers(l1.next,l2.next,carry)
        return ret
        