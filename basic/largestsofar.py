largest_so_far= -1
print 'before', largest_so_far

for num in [21,53,54,74,99]:
    if num> largest_so_far:
        largest_so_far= num
    print largest_so_far, num
    
print 'after', largest_so_far