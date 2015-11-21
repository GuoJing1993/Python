smallest= None
print 'before'

for num in [11,22,33,44,55]:
    if smallest is None:
        smallest=num
    elif smallest >num:
        smallest=num
    print 'smallest is; ', smallest

print 'after'