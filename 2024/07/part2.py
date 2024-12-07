import io
import sys

def get_target(s):
    return int(s.rstrip(':'))

def combinations(i, nums, running_total, target):
    if running_total == target and i == len(nums):
        return True

    if i < len(nums):
        if i == 0:
            return combinations(i+1, nums, nums[i], target)
        else:
            return combinations(i+1, nums, running_total + nums[i], target) or\
                   combinations(i+1, nums, running_total * nums[i], target) or\
                   combinations(i+1, nums, int(str(running_total) + str(nums[i])), target)
    return False

def solve(targets, nums):
    N = len(targets)
    ans = 0
    for i in range(N):
        if combinations(0, nums[i], 0, targets[i]):
            ans += targets[i]
    return ans


with open("input.txt") as file:
    lines = list(map(str.split, list(map(str.rstrip, file.readlines()))))
    targets = [get_target(l[0]) for l in lines]
    nums = [[int(l[i]) for i in range(1, len(l))] for l in lines]
    print(solve(targets, nums))
