nums = [2,1,5,3]
target = 4

def solution(nums, target):
    prev_map = {} # value to the index

    for i,n in enumerate(nums):
        difference = target - n
        if difference in prev_map:
            return [prev_map[difference], i]
        prev_map[n] = i
    return 

(solution(nums, target))