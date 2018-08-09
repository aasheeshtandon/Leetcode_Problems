# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # Two Solutions are provided here.
        ## 1st one is simple to understand but a lot of unnecessary lines of code.
        ### 2nd one is also based on the same idea but a litle tricky to understand in the first go
        
        ######### Solution 1 #########
        if headA is None or headB is None:
            return None
        
        countA = 0
        countB = 0
        
        temp = headA
        while temp:
            countA += 1
            temp = temp.next
        
        temp = headB
        while temp:
            countB += 1
            temp = temp.next
        
        diff = abs(countA - countB)
        
        if countA > countB:
            temp = headA
            while diff:
                temp = temp.next
                diff -= 1
            while temp != headB:
                temp = temp.next
                headB = headB.next
        else:
            temp = headB
            while diff:
                temp = temp.next
                diff -= 1
            while temp != headA:
                temp = temp.next
                headA = headA.next
        return temp
        
        
        ######### Solution 2 #########
            
        if headA is None or headB is None:
            return None
        pa = headA
        pb = headB
        while pa is not pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
        return pa
