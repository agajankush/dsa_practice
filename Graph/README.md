#### Theory

There are 2 main approaches to implement a disjoint set:

1. Quick Find\
    This algorithm has very efficient find operation but a costly union operation.
    ```python
    find(x) -> O(1) 
        Since all the index saves the root
    union(x, y) -> O(n)(best) & O(n^2)(worst)
        Merging 2 sets.
        If we want to merge 2 sets we need to check if there roots is similar.
            If not:
                look for all the index with the root[y] and then change them to root[x]
                this will connect them both.
    
2. Quick Union\
    This algorithm is effecient in a complete sense the max time complexity of this algorithm is O(n)
    ```python
    find(x) -> O(n)
        Check if x != parent[x]
            parent[x] = find(parent[x]) # We recursively look for the parent until we find the parent
        return parent[x]
    
    union(x,y) -> O(n)
        Merging 2 sets\
        In this algorithm we dont have to check all the parents.\
        Just assign parent[parent_y] = x

        