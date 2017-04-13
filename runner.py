import os
os.system("echo 'time,match,val1,val2,len1,len2,len1xlen2' >> results")
for i in xrange(25):
    for j in xrange(25):
        if i != j:
            os.system('python brute.py tests/'+str(i)+'.s tests/'+str(j)+'.s >> results')