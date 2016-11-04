class Solution(object):
    def findNthDigit(self, n):
        # Find max/min number n can fall in
        minnum = 0
        maxnum = 9
        # Find max/min characters n can fall in
        minchars = 0
        maxchars = 9
        # Update max/min characters for n
        while (maxchars < n):
            minnum = maxnum+1
            maxnum = maxnum*10+9
            minchars = maxchars + 1
            maxchars += (maxnum - minnum + 1)*len(str(maxnum))
        # Find difference from min characters
        diff = n - minchars
        # Find actual number of n
        numcount = minnum + diff/len(str(maxnum))
        # Find offset of actual number
        offset = diff%len(str(maxnum))
        return int(str(numcount)[offset])
