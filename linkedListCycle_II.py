# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        slow, fast = head, head
        # Step 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # Cycle detected, now find the entry point
                # Step 2: Reset one pointer to the head
                slow = head
                # Move both pointers at the same speed
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow # or fast, as they are the same at the entry point
        
        # No cycle detected
        return None
