# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find middle, revvverse second, merge
        #1. find middle
        sec, fast = head,head
        while fast and fast.next:
            sec = sec.next
            fast = fast.next.next
        #2. rev sec
        second = sec.next
        prev, sec.next = None, None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        #3. Merge the second with first
        first, second = head,prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1,tmp2