# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        pt = head
        while pt:
            nxt = pt.next
            pt.next = prev
            if prev:
                prev_nxt = prev.next 
                prev.next = nxt
                prev = prev_nxt
            pt = nxt
        