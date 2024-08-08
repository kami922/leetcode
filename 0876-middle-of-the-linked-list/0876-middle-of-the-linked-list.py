# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # temp = head
        # n = 0
        # while temp:
        #     n +=1
        #     temp = temp.next
        # temp = head
        # for i in range(n//2):
        #     temp = temp.next
        # return temp
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow