class DisjointSet:
    def __init__(self,n):
        self.rank=[0]*(n+1)
        self.parent=[i for i in range(n+1)]
    def findUpar(self,node):
        if node == self.parent[node]:
            print(self.parent)
            return node
        self.parent[node]=self.findUpar(self.parent[node])
        return self.parent[node]
    def unionByRank(self,u,v):
        ulp_u=self.findUpar(u)
        ulp_v=self.findUpar(v)
        if ulp_u == ulp_v:
            return
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u]=ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v]=ulp_u
            self.rank[ulp_u]+=1
    
ds = DisjointSet(7)
ds.unionByRank(1, 2)
ds.unionByRank(2, 3)
ds.unionByRank(4, 5)
ds.unionByRank(6, 7)
ds.unionByRank(5, 6)

if ds.findUpar(3) == ds.findUpar(7):
    print("Same")
else:
    print("Not same")

ds.unionByRank(3,7)
if ds.findUpar(3) == ds.findUpar(7):
    print("Same")
else:
    print("Not same")



"""Overall Complexity
Time complexity =m.α(n)
α=alpha
"""
