# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        def revertIndexOfNode(father, curNode, n):
            if curNode:
                index = revertIndexOfNode(curNode, curNode.next, n)
                print("-----------------")
                print(index)
                if index == n:
                    father.next = curNode.next
                return index+1
            else:
                return 1

        
        prenode = ListNode(0)
        prenode.next = head
        revertIndexOfNode(prenode, head, n)
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
l1 = generateList([1])
printList(l1)
printList(s.removeNthFromEnd(l1, 1))
