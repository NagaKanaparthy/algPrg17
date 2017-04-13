def printMatrix(mat,rowName,columnName):
    i = 0
    val = " |   | "
    for c in xrange(len(mat[0])-1):
        if columnName[c] != '\0':
            val += columnName[c]+" | "
        else:
            val += "  |"
    print val
    val = ''
    for row in mat:
        if i == 0:
            val = " | "
        elif rowName[i-1] == '\0':
            val = " | "
        elif i  <= len(rowName):
            val = str(rowName[i-1]) + "| "
        else:
            val = " | "
        for entry in row:
            val += str(entry) + ' | '
        i += 1
        print val

def getLongestSubString(val1 ,val2):
    #add terminating character
    val1 += '\0'
    val2 += '\0'
    #Length of both arrays
    lenN = len(val1)
    lenM = len(val2)
    # Create Matrix that uses val1's range as row and val2 as column
    matrix = [
        [0 for x in xrange(lenM+1)]
        for x in xrange(lenN+1)
    ]

    # Set longest common substring pos relative to val1 
    longestPos,longestLen = 0,0
    #O(N*M)
    for x in xrange(1,lenN+1):
        for y in xrange(1,lenM+1):
            if val1[x-1] == val2[y-1]:
                matrix[x][y] = matrix[x-1][y-1]+1
                if matrix[x][y] > longestLen:
                    longestLen = matrix[x][y]
                    longestPos = x
            else:
                matrix[x][y] = 0

    return val1[longestPos-longestLen:longestLen]

import sys
# Read in file names
fileName1 = sys.argv[1]
fileName2 = sys.argv[2]
# Files
source1 = open(sys.argv[1], "r").read()
source2 = open(sys.argv[2], "r").read()

print getLongestSubString(source1,source2)
