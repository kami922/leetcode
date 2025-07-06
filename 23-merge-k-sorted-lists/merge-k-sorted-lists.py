# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Initialize a min-heap.
        # Python's heapq module implements a min-heap.
        # We'll store tuples of (value, index, ListNode) in the heap.
        # The index is added to handle cases where two nodes might have the same value,
        # as heapq needs to compare the entire tuple and ListNode objects are not
        # directly comparable by default. The index provides a unique tie-breaker.
        min_heap = []
        
        # Populate the heap with the first node from each list
        # Iterate through the input list of linked list heads
        for i, head in enumerate(lists):
            if head:
                # Push a tuple (node_value, list_index, node_object) onto the heap.
                # The heap will prioritize based on node_value.
                heapq.heappush(min_heap, (head.val, i, head))

        # Create a dummy node to simplify the construction of the merged list.
        # This avoids special handling for the head of the merged list.
        dummy_head = ListNode(0)
        current_tail = dummy_head # This pointer will always point to the last node of the merged list

        # Process nodes from the heap until it's empty
        while min_heap:
            # Pop the smallest element from the heap.
            # it[0] is the value, it[1] is the list_index, it[2] is the ListNode object.
            val, list_idx, node = heapq.heappop(min_heap)

            # Append the popped node to the merged list
            current_tail.next = node
            current_tail = node # Move the current_tail pointer to the newly added node

            # If the popped node has a next node, push it onto the heap.
            # This ensures we always have the next smallest element from that list available.
            if node.next:
                heapq.heappush(min_heap, (node.next.val, list_idx, node.next))
        
        # The merged list starts from dummy_head.next
        return dummy_head.next

