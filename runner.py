import os
for i in xrange(25):
    for j in xrange(25):
        if i != j:
            os.system('python brute.py tests/'+str(i)+'.s tests/'+str(j)+'.s >> results')