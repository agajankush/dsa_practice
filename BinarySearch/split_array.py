def splitArray(nums, k):
    start = 0
    end = 0
    for n in nums:
        start = max(start, n)
        end = end + n
    
    while start <= end:
        mid = start + (end-start) // 2
        sum = 0
        pieces = 1
        
        for n in nums:
            sum += n
            if sum > mid:
                pieces += 1
                sum = n
        
        if pieces <= k:
            end = mid
        else:
            start = mid + 1
    
    return start