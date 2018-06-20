class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = []
        self.dict = {}
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        try:
            self.dict[key]
            self.cache.append(key)
            if len(self.cache) > self.capacity:
                self.cache = self.cache[1:]
            return self.dict[key]
        except KeyError:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        try:
            self.dict[key]
            self.dict[key] = value
            self.cache.append(key)
            if len(self.cache) > self.capacity:
                del self.dict[key]
                self.cache = self.cache[1:]
        except KeyError:
            self.dict[key] = value
            self.cache.append(key)
            if len(self.cache) > self.capacity:
                del self.dict[key]
                self.cache = self.cache[1:]