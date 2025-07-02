"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Copies a linked list where each node has a next pointer and a random pointer.
        This solution uses an O(1) space complexity approach by interleaving
        the copied nodes with the original nodes.

        Algorithm Steps:
        1. Interleave copied nodes: For each original node, create its copy and
           insert it immediately after the original node.
           Original: A -> B -> C
           Interleaved: A -> A' -> B -> B' -> C -> C'
        2. Assign random pointers to copied nodes: Traverse the interleaved list.
           For each original node 'curr', its copy is 'curr.next'.
           If 'curr' has a random pointer to 'curr.random', then the copy 'curr.next'
           should have its random pointer point to the copy of 'curr.random',
           which is 'curr.random.next'.
        3. Separate the original and copied lists: Traverse the interleaved list
           again. Extract the copied nodes into a new list and restore the
           original list's next pointers.

        Args:
            head: The head of the original linked list.

        Returns:
            The head of the deep copy of the linked list.
        """
        
        # Handle the edge case where the input list is empty.
        if head is None:
            return None
        
        # Step 1: Interleave copied nodes with original nodes.
        # Traverse the original list. For each node, create its copy
        # and insert it between the original node and its next node.
        temp = head
        while temp is not None:
            # Create a new node with the same value as the current original node.
            copy_node = Node(temp.val)
            
            # Link the new copy node to the original's next node.
            copy_node.next = temp.next
            
            # Link the original node to its new copy.
            temp.next = copy_node
            
            # Move 'temp' to the next original node (which is now after the copy).
            temp = copy_node.next
        
        # Step 2: Assign random pointers to the copied nodes.
        # Traverse the interleaved list. For each original node 'temp',
        # its copy is 'temp.next'.
        temp = head
        while temp is not None:
            # If the original node has a random pointer,
            # then its copy's random pointer should point to the copy
            # of the node that the original's random pointer points to.
            # The copy of 'temp.random' is 'temp.random.next'.
            if temp.random:
                temp.next.random = temp.random.next
            
            # Move 'temp' to the next original node (skipping the copy).
            temp = temp.next.next
            
        # Step 3: Separate the original and copied lists.
        # Use a dummy node to easily build the new copied list.
        dummy_head = Node(0) # Dummy node for the new copied list
        res_ptr = dummy_head # Pointer to build the result list
        
        # Reset 'temp' to the head of the original interleaved list.
        temp = head 
        
        while temp is not None:
            # 'copy_node' is the node immediately after the current original 'temp'.
            copy_node = temp.next
            
            # Link the result list to the current copied node.
            res_ptr.next = copy_node
            
            # Restore the original list's 'next' pointer by skipping the copy.
            temp.next = copy_node.next
            
            # Advance the result list pointer.
            res_ptr = res_ptr.next
            
            # Advance the original list pointer.
            temp = temp.next
            
        # The head of the copied list is after the dummy node.
        return dummy_head.next
