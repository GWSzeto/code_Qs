const findPosition = (stack, num, nums, position) => {
    const latest = stack.pop()
    if (position == "start" && nums[latest] <= num) return (latest + 1)
    if (position == "end" && nums[latest] >= num) return (latest - 1)
    findPosition(stack, num, nums)
}

const findUnsortedSubarray = nums => {
    let firstPosition = 0 
    let secondPosition = 0
    let stack = []
    let pos = 0
    for (num of nums) {
        if (stack && nums[stack[-1]] > num) {
            firstPosition = findPosition(stack, num, nums, "start")
            break
        }
        stack.push(pos)
        pos++
    }

    stack = []
    pos = nums.length - 1

    for (num of nums.reverse()) {
        if (stack && nums[stack[-1]] < num) {
            secondPosition = findPosition(stack, num, nums, "end")
            break
        }
        stack.push(pos)
        pos--
    }

    return (secondPosition - firstPosition)
}