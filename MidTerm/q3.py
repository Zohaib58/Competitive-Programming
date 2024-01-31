from itertools import combinations
from sys import stdin

def bin(subsets, target_sum):
    left, right = 0, len(subsets) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_sum , mid_subset= subsets[mid]

        if mid_sum == target_sum:
            return mid
        elif mid_sum < target_sum:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def SubSameSum(nums):
    n = len(nums)
    half = n // 2
    subsets = []
    
    for i in range(1, half + 1):

        for combo in combinations(nums[:half], i):
            subsets.append((sum(combo), combo))
    subsets.sort()

    for i in range(n - half + 1):
        for combo in combinations(nums[half:], i):
            target_sum = sum(combo)
            index = bin(subsets, target_sum)
            if index != -1:
                return subsets[index][1], combo

    return "Impossible"

def Sol(case_num, nums):
    first_subset, second_subset = SubSameSum(nums)

    result = []
    result.append("Case #{}:".format(case_num))
    if first_subset != "Impossible":
        result.append(" ".join(map(str, first_subset)))
        result.append(" ".join(map(str, second_subset)))
    else:
        result.append("Impossible")
    
    return "\n".join(result)


lines = stdin.read().splitlines()

numCases = int(lines[0])
current_line = 1

for case in range(1, numCases + 1):
    n = lines[current_line][0]
    n, *nums = map(int, lines[current_line].split())
    current_line += 1
    print(Sol(case, nums))
