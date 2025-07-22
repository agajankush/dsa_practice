class UnionFind():
    def __init__(self, size):
        self.size = size
        self.parent = [i for i in range(size)]
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.parent[x]
        root_y = self.parent[y]
        
        if root_x != root_y:
            self.parent[root_y] = root_x