# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = []
        while head:
            s.append(head.val)
            head = head.next
        l = len(s)
        m = l // 2
        if m == l / 2:
            return s[:m] == s[m:][::-1]
        return s[:m] == s[m+1:][::-1]
        