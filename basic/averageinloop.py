count=0
sum=0
print 'before', count

for value in [32, 33, 53, 56, 35] :
 count= count + 1
 sum= sum + value
 print count, value, sum
 
print 'after'
print 'average is:', sum/count
 