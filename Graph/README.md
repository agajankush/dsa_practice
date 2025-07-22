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

3. Union Rank\
    Both the above algorithm can be optimised. In the Union example if we keep selecting the wrong parent we will have a time complexity of O(n) but if we can optimise it then it would help.
    For example if we want to merge 2 trees and if we know the height of the tree we can use that height as the parent.
    This will eliminate the size increase when merging also will help optimizing the find.
    Look at leetcode for the example in the graph section.
    ```python
    find(x) -> O(logN)
    def find(x):
        if x != parent[x]:
            parent[x] = find[parent[x]]
        return parent[x]
    union(x,y) -> O(logN)
    def union(x,y):
        parent_x = find(x)
        parent_y = find(y)
        We keep track of a rank list which will be set to 1 at first.\
        AS we keep merging increase the rank of the parent node by 1 only if they are equal
        