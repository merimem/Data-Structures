class LRUCache:
    def __init__(self, deque, hashSet = None, cSize= None):
        self.deque = deque;
        self.hashSet = hashSet;
		self.cSize = cSize;

LRUCache()