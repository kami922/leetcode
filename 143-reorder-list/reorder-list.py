# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        n = 0
        track_stack = []
        temp = head
        while temp:
            track_stack.append(temp)
            temp = temp.next
            n += 1

        temp = head

        for i in range(n // 2):
            str_node = temp.next
            last_node_from_stack = track_stack.pop()
            temp.next = last_node_from_stack
            last_node_from_stack.next = str_node
            temp = str_node

        temp.next = None
        
            