# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Detailed drawing is key


        if not head or not head.next:   return head

        # FINDING MIDDLE
        L = F = S = head
        while F and F.next:     F, S = F.next.next, S.next      

        # REVERSING SECOND HALF LL
        prev, curr = None, S
        while curr:
            future = curr.next
            curr.next = prev
            prev, curr = curr, future
        R = prev

        # REWIRING LL Using 2 pointers
        while L != S:   #draw even case and see why its not != R
            L.next, L = R, L.next
            R.next, R = L, R.next
        L.next = None
        return head

        
            