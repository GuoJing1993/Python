#please parse out the main address: From peterhsu@yahoo-inc.com Sat Jan 5 09:14:16 2008

line='From peterhsu@yahoo-inc.com Sat Jan 5 09:14:16 2008'
a= line.split(' ')
email=a[1]
piece= email.split("@")
print piece[1]