def canFinish(numCourses, prerequisites):
    preMap = {i: [] for i in range(numCourses)}

    for crs, pre in prerequisites:
        preMap[crs].append(pre)

    visitSet = set()

    def dfs(crs):
        if crs in visitSet:
            return False
        if preMap[crs] == []:
            return True

        visitSet.add(crs)
        for i in preMap[crs]:
            if not dfs(i):
                return False
        visitSet.remove(crs)
        preMap[crs] = []
        return True

    for crs in range(numCourses):
        if not dfs(crs):
            return False
    return True
