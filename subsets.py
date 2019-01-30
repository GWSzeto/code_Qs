def subsets(nums):
    solution = []
    def dfs(start, path):
        solution.append(path)
        for i in range(start, len(nums)):
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])

    return solution

print(subsets([3,1,2]))
