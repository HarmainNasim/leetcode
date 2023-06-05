class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d= {}
        p= set()
        for i,j in paths:
            d[i]=j
            p.add(i)
            p.add(j)
        for i in p:
            if i not in d.keys():
                return i
        
