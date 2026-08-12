# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()

        tail = head

        while tail:
            if tail not in seen:
                seen.add(tail)
            else:
                return True
            tail = tail.next
        
        return False



        