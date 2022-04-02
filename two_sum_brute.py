nums = [2,1,5,3]
target = 4

def solution(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                if i != j:
                    return i,j

print(solution(nums, target))