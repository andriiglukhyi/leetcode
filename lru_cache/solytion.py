class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.counter = 0
        self.bucket = {}
        self.last = None
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        try:
            return self.bucket[key]
        except KeyError:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        lst = list(self.bucket.keys())
        if self.counter + 1 > self.capacity:
            del self.bucket[lst[0]]            
        self.bucket[key] = value
        self.last = key
        print(  self.bucket)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)