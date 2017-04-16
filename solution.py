import os,random,string,subprocess,sys

#Functions
def genRandStr(length):
    return ''.join(random.choice(
        #string.ascii_uppercase + \
        string.ascii_lowercase # + \
        #string.digits
        ) for _ in range(length))

def runSingleTest(length):
    #create Test Files
    testString1 = genRandStr(length)
    testString2 = genRandStr(length)
    tempFileName1 = 'temp1.csv'
    tempFileName2 = 'temp2.csv'
    open(tempFileName1,'w').write(testString1)
    open(tempFileName2,'w').write(testString2)
    #Run test
    fileToExec = 'brute.py'
    if sys.platform.startswith('win'):
        fileToExec = '.\\brute.py '
    arguements = 'python '+ fileToExec + ' ' +\
     tempFileName1 + ' ' + tempFileName2
    out = subprocess.check_output(arguements,shell=False) 
    #clean up
    os.remove(tempFileName1)
    os.remove(tempFileName2)
    return out

#Main program
#grab length
maxLen = sys.argv[1]
#Execute Tests
res = ''
for len in range(int(maxLen)+1):
    if(len > 0):
        res += runSingleTest(len).strip() + '\n'
print res
#Output Result to file
resultFile = open('result.csv','w')
resultFile.write('time,match,val1,val2,len1,len2,len1xlen2\n')
resultFile.write(res.strip())