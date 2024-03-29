from copy import deepcopy

def combination_sum_helper(nums, start, result, remainder, combination):

    if(remainder == 0):
        result.append(deepcopy(combination))
        return
    elif( remainder <0):
        return # sum exceeded the target
    for i in range(start, len(nums)):
        combination.append(nums[i])
        combination_sum_helper(nums, i+1, result, remainder-nums[i], combination)
        #backtrack
        combination.pop()


def combination_sum(nums, target):
    result = []
    combination_sum_helper(nums,0, result, target,[])
    print(result)

print(combination_sum([11,1,3,2,6,1,5], 8))