# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        index = -1

        tail = head

        while tail:
            index += 1
            if tail not in seen:
                seen.add(tail)
            else:
                return True
            tail = tail.next
        
        return False



        