class QuickFind():
    def __init__(self, size):
        self.size = size
        self.parent = [i for i in range(size)]
    
    # Find the parent of the element x
    # O(n) time complexity
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    # Merging two sets containing x and y
    # O(n) time complexity
    def union(self,x,y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        
        if parent_x != parent_y:
            self.parent[parent_y] = x
    
    def connected(self, x, y):
        return self.parent[x] == self.parent[y]