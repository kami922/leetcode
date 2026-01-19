# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        temp = head
        back = None
        curr = head
        ins = head
        count = 0

        # Count the length of the list
        while ins:
            count += 1
            ins = ins.next

        k = k % count  # Adjust k to avoid unnecessary rotations

        while temp and k > 0:
            if not temp.next:
                temp.next = curr  # Make it a circular list temporarily
                back.next = None  # Break the link to rotate
                head = temp
                curr = temp
                k -= 1

            back = temp
            temp = temp.next

        return curr
        