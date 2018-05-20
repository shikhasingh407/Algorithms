def maxSum(nums, left, right):
    maxLeftBorderSum = float("-inf")
    maxRightBorderSum = float("-inf")
    i = 0
    j = 0
    center = 0
    if left == right:
        # if nums[left] > 0 :
        return nums[left]
        # else:
        #    return 0

    center = int((left + right) / 2)
    maxLeftSum = maxSum(nums, left, center)
    maxRightSum = maxSum(nums, center + 1, right)

    leftBorderSum = 0
    rightBorderSum = 0

    for i in range(center, left, i - 1):
        leftBorderSum = leftBorderSum + nums[i]
        if leftBorderSum > maxLeftBorderSum:
            maxLeftBorderSum = leftBorderSum

    for j in range(center + 1, right, j + 1):
        rightBorderSum = rightBorderSum + nums[j]
        if rightBorderSum > maxRightBorderSum:
            maxRightBorderSum = rightBorderSum

    print (maxLeftBorderSum)
    print (maxRightBorderSum)
    print (maxLeftSum)
    print (maxRightSum)

    print (max(maxLeftSum, maxRightSum, maxLeftBorderSum + maxRightBorderSum))

nums = [-2, -1]
maxSum(nums, 0 , 1)