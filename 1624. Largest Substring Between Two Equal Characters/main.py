class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        list0=[]
        list1=[]
        list2=[]
        for i in range(len(s)):
            if s.count(s[i])>1 and s[i] not in list0:
                list0.append(s[i])
                list1.append(i)
        for j in list0:
            for i in range(len(s)-1,-1,-1):
                if s[i]==j:
                    list2.append(i)
                    break
        list3=[]
        for i in range(len(list1)):
            list3.append(list2[i]-list1[i]-1)
        if len(list0)>0:
            return max(list3)
        else:
            return -1
