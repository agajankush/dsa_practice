class QuickFind():
    def __init__(self, size):
        self.size = size
        self.root = [i for i in range(size)]
    
    # Find the root of the element x
    # O(1) time complexity
    def find(self, x):
        return self.root[x]
    
    # Merging two sets containing x and y
    # O(n) time complexity
    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            for i in range(self.size):
                if self.root[i] == root_y:
                    self.root[i] = root_x
    
    def connected(self, x, y):
        return self.root[x] == self.root[y]