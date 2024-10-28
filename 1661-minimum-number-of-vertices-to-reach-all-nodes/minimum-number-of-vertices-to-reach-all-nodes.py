class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        #find the set of vertices (smallest) from which all nodes in the graph are reachable

        #basically in a directed acyclic graph, for smallest set of verticies with which all nodes in the
        # graph are reachable. the set of vertices would be the ones not connected most times

        visited = set()
        for i in edges:
            visited.add(i[1]) #add destination node into the visited list.
        
        result = []
        for j in range(n): #iterate over all nodes
            if j not in visited:
                result.append(j)
        
        return result


            