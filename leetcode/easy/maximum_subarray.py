'''
#53 easy
'''
# LINEAR
def maxSubArray(nums):
    # take the first index, this will take care of a list with just one number
    maxSub = nums[0] 
    # this will update with the sums and have the largest at the end
    currSum = 0 

    for n in nums:
        # we will never take the leading negative numbers
        if currSum < 0: 
            # reset it
            currSum = 0 
        # keep adding up the numbers
        currSum += n
        # with each iteration we update the maximum sub array so when we reset cur sum, at the end we will just have the highest possible number
        maxSub = max(maxSub, currSum)
    return maxSub

# test
print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))