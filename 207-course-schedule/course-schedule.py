class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #prereq[i] = [ai, bi] take bi before taking ai
# Step 1: populate a prerequisite map containing courses and its respective prerequisites
        premap = {i: [] for i in range(numCourses)} #initilize the map for each course

  # Step 2: Populate the prerequisite map
        for course, pre  in prerequisites: 
            premap[course].append(pre)
        
        visitset = set() #contains the visited courses ( will help in detecting a loop/cycle a vertex visited twice)

         # Helper function to perform DFS for cycle detection
        def dfs(course):
            if course in visitset:  # If the course is already in the current DFS path, it means a cycle is detected
                return False

            if premap[course] == []:  # If there are no prerequisites for this course, return True
                return True

            visitset.add(course)  # Marking the course as visited in the current path

            for pre in premap[course]: # Traverse all prerequisites of the current course
            # If any prerequisite leads to a cycle, return False
                if not dfs(pre):
                    return False

             # After visiting all prerequisites, remove the course from the path
            visitset.remove(course)

            # If no cycle is found, return True
            premap[course] = []
            return True
        
        # Step 3: Iterate over each course and run DFS
        for course in range(numCourses):
            if not dfs(course):
                return False

  # If no cycles are found after checking all courses, return True
        return True
        