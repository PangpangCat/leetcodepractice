class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 1009  # prime number 有1009个bucket
        self.bucket = [bucket() for i in range(self.m)]

    def _hash(self, key):
        return key % self.m  # 对key值取余

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucketIndex = self._hash(key)
        self.bucket[self._hash(key)].insert(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.bucket[self._hash(key)].delete(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.bucket[self._hash(key)].exist(key)


class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class bucket(object):
    def __init__(self):
        self._head = None

    def insert(self, item):
        if not self.exist(item):
            node = Node(item)
            node.next = self._head
            self._head = node

    def delete(self, item):
        if not self.exist(item):
            return
        pre = None
        cur = self._head
        while cur != None:
            if cur.item == item:
                if pre == None:
                    self._head = cur.next
                    return
                else:
                    pre.next = cur.next
            pre = cur
            cur = cur.next

    def exist(self, item):
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)