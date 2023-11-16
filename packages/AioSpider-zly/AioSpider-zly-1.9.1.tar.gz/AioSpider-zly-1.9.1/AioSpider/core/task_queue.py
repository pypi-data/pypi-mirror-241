from collections import deque


class Queue(deque):
    
    def put(self, value):
        if isinstance(value, list):
            self.extend(value)
        else:
            self.append(value)
    
    def get(self):
        return self.popleft()
    
    def empty(self):
        return True if len(self) == 0 else False
    
    
class RedisQueue:
    
    def __init__(self, conn):
        self.conn = conn
    
    def put(self, value):
        pass
    
    def get(self):
        pass
