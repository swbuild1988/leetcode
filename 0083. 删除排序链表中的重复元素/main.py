# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        preNode = ListNode(0)
        preNode.next = head
        father = preNode
        while head.next:
            # 如果下一个节点和当前节点值一样
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        
        return preNode.next



def generateList(l):
    prenode = ListNode(0)
    lastnode = prenode
    for val in l:
        lastnode.next = ListNode(val)
        lastnode = lastnode.next
    return prenode.next


def printList(l):
    while l:
        print("%d, " % (l.val), end='')
        l = l.next
    print('')


s = Solution()
l1 = generateList([1, 1, 2, 2, 5])
printList(s.deleteDuplicates(l1))
