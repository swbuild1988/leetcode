# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        n = 0
        curNode = head
        while curNode:
            n += 1
            curNode = curNode.next
        if n == 0:
            return ListNode(0).next
        k = k % n

        if k == 0:
            return head

        prenode = ListNode(0)
        curNode = head
        index = 0
        while index < n:
            index += 1
            print(index, n-k)
            if index == n - k:
                prenode.next = curNode.next
                curNode.next = None
                break
            else:
                curNode = curNode.next
        
        curNode = prenode.next
        while curNode.next:
            curNode = curNode.next
        curNode.next = head

        return prenode.next
        


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
l1 = generateList([1, 2, 3, 4, 5])
printList(s.rotateRight(l1, 2))
