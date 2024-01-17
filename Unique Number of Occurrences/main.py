class Solution(object):
    def uniqueOccurrences(self, arr):
        data = defaultdict(int)
        for n in arr:
            data[n] += 1
        outdata = defaultdict(int)
        for key in data:
            outdata[data[key]] += 1
            if outdata[data[key]] == 2:
                return False
        return True
      
