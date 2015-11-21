usertypehours=raw_input('Enter Hours:')
usertyperate=raw_input('Enter Rate:')

x=int(usertypehours)
y=int(usertyperate)

if x>40:
    print 40*y+(x-40)*(y+5)
else:
    print x*y
    