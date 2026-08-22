# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
        l1values = []
        l2values = []

        print(l1)

        while l1:
            l1values.append(l1.val)
            l1 = l1.next

        while l2:
            l2values.append(l2.val)
            l2 = l2.next

        num1 = int(''.join(map(str, l1values[::-1])))
        num2 = int(''.join(map(str, l2values[::-1])))
        
        num = num1 + num2
        num = str(num)[::-1]
        
        answer = list(map(int, num))

        
        dummy = ListNode()
        current = dummy 

        for val in answer:
            current.next = ListNode(val)
            current = current.next
        
        print(dummy)
        print(dummy.next)

        return dummy.next 

    
    
