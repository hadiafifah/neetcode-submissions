# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # issue: n might be greater than length of list
        # therefore we first need to figure out how long the list is
        # then find the true value we need to go to (N - n)
        total_nodes = 0
        curr = head

        while curr:
            total_nodes += 1
            curr = curr.next

        remove_index = total_nodes - n
        if remove_index == 0:
            return head.next

        curr = head
        for i in range(total_nodes - 1):
            if (i + 1) == remove_index:
                curr.next = curr.next.next
                break
            curr = curr.next

        return head
        