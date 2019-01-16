def sortColors(nums):
    red = 0
    blue = len(nums) - 1
    for i in range(len(nums)):
        while(nums[i] == 2 and i < blue):
            nums[i], nums[blue] = nums[blue], nums[i]
            blue -= 1
        while(nums[i] == 0 and i > red):
            nums[i], nums[red] = nums[red], nums[i]
            red += 1

sortColors([2,0,2,1,1,0])
