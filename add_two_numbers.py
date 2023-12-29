# https://leetcode.com/problems/add-two-numbers/?envType=list&envId=xyknlrg2
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number_parts = [l1.val]
        current = l1
        while current.next is not None:
            current = current.next
            number_parts.append(current.value)

        num1 = int("".join(number_parts))
        
        number_parts = [l2.value]
        current = l2
        while current.next is not None:
            current = current.next
            number_parts.append(current.value)
            
        num2 = int("".join(number_parts))
        
        sum = num1 + num2
        digits = list(sum)
        
        current = 
        for digit in digits:
            
        
 
        

