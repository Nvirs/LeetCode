class RandomizedSet(object):

    def __init__(self):
        self.vals = {}
        self.idxs = []

    def insert(self, val):
        if val in self.vals : return False
        self.vals[val] = len(self.idxs)
        self.idxs.append(val)
        return True
        

    def remove(self, val):
        if val in self.vals:
            lst = self.idxs[-1]
            pos = self.vals[val]

            self.vals[lst] = pos
            movedRight = pos
            self.idxs[movedRight] = lst
            updateRight = lst
            
            deletePrev = self.vals.pop(val)
            deleteValAndIdx = self.idxs.pop()
            return True
        return False
    def getRandom(self):
        randomIdx = random.choice(self.idxs)
        return randomIdx

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
