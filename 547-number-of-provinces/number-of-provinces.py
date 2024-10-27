from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        #return total number of provinces: provice is a group directly or indirectly connected. 
        #so we need to find the number of components in a graph       

        #using stack dfs
        n = len(isConnected) #get length of nodes
        visited = set() 
        components = 0

        for i in range(n):
            if i not in visited:
                stack = [i]
                
                while stack:
                    node = stack.pop()
                    visited.add(node)
                    for j in range(n):
                        if j not in visited and isConnected[node][j] ==1:
                            stack.append(j)
                        
                components+=1
        
        return components

        #using recursion
        
        # def dfs(i):
        #     visited.add(i)
        #     for j in range(n):
        #         if j not in visited and isConnected[i][j] == 1:  #theres an edge i, j where i is directly connected to j
        #             dfs(j)

        # n = len(isConnected) #get length of nodes
        # visited = set() 
        # components = 0

        # for i in range(n): # 0 to n-1
        #     if i not in visited:
        #         dfs(i)
        #         components+=1
        
        # return components

        # #time complexity O(n^2)        