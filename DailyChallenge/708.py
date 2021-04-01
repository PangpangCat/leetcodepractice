"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        # case 1：edge 列表为空
        if head == None:
            head = Node(insertVal, None)
            head.next = head  # 新建的结点指向它本身
            return head

        # Two pointer prev and succ

        prev = head
        cur = head.next

        while True:
            # while True如果使用这一种的话，在循环内就需要一个方式把whileTrue打破。
            # 这里很难定义一个清晰的跳出环境， 只能在内部把第2，3，4的情况都考虑了之后再Break掉。
            # case 2： 1--->3 insert 2, 1-->2-->3
            if prev.val <= insertVal <= cur.val:
                # prev.next = Node(insertVal, cur)
                break
            # case 3： 5--->1 insert 7， 5-->7-->1
            elif prev.val > cur.val:
                if insertVal >= prev.val or insertVal <= cur.val:
                    # prev.next = Node(insertVal, cur)
                    break

            # case 4: else 3 -->3-->3 insert 7, 3 -->3-->3-->7 这种情况下需要已经转了一圈的
            prev = prev.next  # 把这两个条件放在前面，就会让两个指针先兜一圈 然后再进入case4的判定。
            cur = cur.next

            if prev == head:
                # prev.next = Node(insertVal, cur)
                break

        new_node = Node(insertVal)
        new_node.next = cur
        prev.next = new_node
        return head


#Time : O(n) 因为case4的情况下需要循环n个节点， n是node数
# Space: O(1) 因为占用常数额外内存