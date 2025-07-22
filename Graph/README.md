#### Theory

There are 2 main approaches to implement a disjoint set:

1. Quick Find
    This algorithm has very efficient find operation but a costly union operation.
    find(x) -> O(1) 
        Since all the index saves the root
    union(x, y) -> O(n)
        Merging 2 sets.
        If we want to merge 2 sets we need to check if there roots is similar.
            If not:
                look for all the index with the root[y] and then change them to root[x]
                this will connect them both.
2. Quick Union
