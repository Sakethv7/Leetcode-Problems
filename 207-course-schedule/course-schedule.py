from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #BFS- enque and deque
        graph = defaultdict(list) #for adjacency list 
        in_degree = [0] * numCourses  #number of incoming edges coming to a node/vertex 
        
        for course, pre in prerequisites:
            graph[pre].append(course)  # pre is a prerequisite for course
            in_degree[course] += 1  # Increase the in-degree of the course

        # Step 2: Initialize the queue with courses that have 0 in-degree
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        # Step 3: Count of processed courses
        processed_courses = 0 #courses that have been done without violating prereqs
        
        # Step 4: BFS traversal
        while queue:
            course = queue.popleft()
            processed_courses += 1  # Mark the course as processed
            
            # Reduce the in-degree of each neighbor
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                
                # If in-degree becomes 0, add the neighbor to the queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 5: If all courses are processed, return True; otherwise, return False
        return processed_courses == numCourses



#DFS recursion:
# # Step 1: populate a prerequisite map containing courses and its respective prerequisites
#         premap = {i: [] for i in range(numCourses)} #initilize the map for each course

#   # Step 2: Populate the prerequisite map
#         for course, pre  in prerequisites: 
#             premap[course].append(pre)
        
#         visitset = set() #contains the visited courses ( will help in detecting a loop/cycle a vertex visited twice)

#          # Helper function to perform DFS for cycle detection
#         def dfs(course):
#             if course in visitset:  # If the course is already in the current DFS path, it means a cycle is detected
#                 return False

#             if premap[course] == []:  # If there are no prerequisites for this course, return True
#                 return True

#             visitset.add(course)  # Marking the course as visited in the current path

#             for pre in premap[course]: # Traverse all prerequisites of the current course
#             # If any prerequisite leads to a cycle, return False
#                 if not dfs(pre):
#                     return False

#              # After visiting all prerequisites, remove the course from the path
#             visitset.remove(course)

#             # If no cycle is found, return True
#             premap[course] = []
#             return True
        
#         # Step 3: Iterate over each course and run DFS
#         for course in range(numCourses):
#             if not dfs(course):
#                 return False

#   # If no cycles are found after checking all courses, return True
#         return True
        