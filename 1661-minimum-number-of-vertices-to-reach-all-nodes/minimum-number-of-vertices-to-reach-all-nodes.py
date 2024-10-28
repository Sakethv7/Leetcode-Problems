class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        #find the set of vertices (smallest) from which all nodes in the graph are reachable

        #basically in a directed acyclic graph, for smallest set of verticies with which all nodes in the
        # graph are reachable. the set of vertices would be the ones that do not have any incoming edges

        visited = set()
        for i in edges: #edges is a list given, that has the edges that are connected where dges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.
        
            visited.add(i[1]) #add destination node into the visited list.
        
        result = []
        for j in range(n): #iterate over all nodes 
            if j not in visited: # if a node is not in visited set that means it is a node with no incoming edge
                result.append(j) 
        
        return result  


            