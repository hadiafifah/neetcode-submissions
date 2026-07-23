class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        finalReturnedList = []
        m = len(strs)
        repSetArray = []

        for i in range(m):
            repSetArray.append({})
            for char in strs[i]:
                if char in repSetArray[i]:
                    repSetArray[i][char] += 1
                else:
                    repSetArray[i][char] = 1

        visited = [False] * m
        for i in range(m):
            if visited[i]:
                continue
            currListToAdd = [strs[i]]
            visited[i] = True
            for j in range(i+1,m):
                if (repSetArray[i] == repSetArray[j] and (not visited[j])):
                    currListToAdd.append(strs[j])
                    visited[j] = True
            finalReturnedList.append(currListToAdd)
        return finalReturnedList

            