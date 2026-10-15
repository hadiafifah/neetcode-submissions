class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = [[]for i in range(numCourses)]
        indegree = [0] * numCourses

        # create indegree count array and prerequisite map
        # why do we need prereq map and indegree count?
        # because we need to know both the prerequisites for a given course, AND
        # how many courses IT is a prereq for (indegree count)
            # when a course's indegree is 0
        for nxt, pre in prerequisites:
            indegree[nxt] += 1
            prereq_map[pre].append(nxt)
        
        res = []

        # calling dfs on a node means it's takeable from where we are
        def dfs(node):
            res.append(node) # if is reachable, add it to our current path
            indegree[node] -= 1 # we got here from somewhere, so after visiting we take down this edge

            # for each neighbor of the current node
            for neighbor in prereq_map[node]:
                # subtract current node from its indegree
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    dfs(neighbor)

        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)

        return res if len(res) == numCourses else []
