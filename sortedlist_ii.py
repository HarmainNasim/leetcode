# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to handle cases where the head itself is a duplicate.
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head
        
        while cur:
            # Check if there are duplicates.
            if cur.next and cur.next.val == cur.val:
                # Skip duplicates.
                while cur.next and cur.next.val == cur.val:
                    cur = cur.next
                prev.next = cur.next  # Remove duplicates by adjusting pointers.
            else:
                prev = prev.next  # Move the pointers only if no duplicates found.
            cur = cur.next  # Move the current pointer forward.
        
        return dummy.next
