def steps_to_zeroes(n, count):
    if n == 0:
        return count
    
    if n% 2 == 0:
        return steps_to_zeroes(n//2, count+1)
    else:
        return steps_to_zeroes(n-1, count + 1)
    
print(steps_to_zeroes(100, 0))