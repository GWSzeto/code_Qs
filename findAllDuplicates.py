def findDuplicates(nums):
    solution = []
    for num in nums:
        if nums[abs(num)-1] < 0:
            solution.append(abs(num))
        else:
            nums[abs(num)-1] *= -1

    return solution

print(findDuplicates([4,3,2,7,8,2,3,1]))
