# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        myset = []
        for n in lists:
            while n:
                myset.append(n.val)
                n = n.next
        myset.sort()
        cur = res = ListNode()
        for k in myset:
            cur.next = ListNode(k)
            cur = cur.next
        return res.next