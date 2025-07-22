'''
Example:
    parent = [0,1,2,3,4,5,6]
    after connecting (0,1)
    parent = [0,0,2,3,4,5,6]
    now whwn we connect 1 and 2
    parent = [0,0,0,3,4,5,6]
    
'''
class QuickFind():
    def __init__(self, size):
        self.size = size
        self.parent = [i for i in range(size)]
    
    # Find the parent of the element x
    # O(n) time complexity
    def find(self, x):
        while self.parent[x] != x:
           x = self.parent[x]  # Path compression
        return x
    
    # Merging two sets containing x and y
    # O(n) time complexity
    def union(self,x,y):
        parent_x = self.find(x) # x = 1 -> 0
        parent_y = self.find(y) # y = 2 -> 2
        
        if parent_x != parent_y:
            self.parent[parent_y] = parent_x
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)