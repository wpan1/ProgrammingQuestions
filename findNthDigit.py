class Solution(object):
    def findNthDigit(self, n):
        minnum = 0
        maxnum = 9
        minchars = 0
        maxchars = 9
        while (maxchars < n):
            minnum = maxnum+1
            maxnum = maxnum*10+9
            minchars = maxchars + 1
            maxchars += (maxnum - minnum + 1)*len(str(maxnum))
        diff = n - minchars
        numcount = minnum + diff/len(str(maxnum))
        offset = diff%len(str(maxnum))
        return int(str(numcount)[offset])
