from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #using DFS with recursion
        # or using dfs with stack(iterative)
        
        # Using stack
        if source == destination:
            return True
        
        graph = defaultdict(list) #get a list defined as a dictionary

         # Build the adjacency list from the given edges
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u) #since it is a bi directional graph

        seen = set() #hash set to check if there are no redundant or duplicate nodes
        seen.add(source) #Mark the source node as visited

        stack = [source] #initilize a stack for DFS, strating with source node 

        # Perform DFS using the stack
        while stack:
            node = stack.pop() #pop most recently added node

            # If the current node is the destination, a path exists
            if node == destination:
                return True
            
              # Traverse all neighbors of the current node
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
                    
          # If the loop completes without finding the destination, return False 
        return False