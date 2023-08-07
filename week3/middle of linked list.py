# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        temp = head
        while head.next:
            length += 1
            head = head.next
        
        new_node = temp
        for i in range((length+1)//2):
            new_node = new_node.next
        return new_node