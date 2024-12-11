def to_nums(s):
    s = s.rstrip()
    s = s.split()
    return [int(x) for x in s]

iter_count = 75

def count_of_digits_even(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count % 2 == 0

def split_num(n):
    s = str(n)
    a = 0
    b = 0
    for i in range(0, len(s) // 2):
        a = a*10 + int(s[i])
    for i in range(len(s) // 2, len(s)):
        b = b*10 + int(s[i])
    return (a, b)

dp = {}

def recurse(n, i):
    x = i
    if (n, x) in dp:
        return dp.get((n, x))
    if i == iter_count:
        return 0
    if n == 0:
        dp[(n, x)] = recurse(1, i+1)
        return dp.get((n, x))
    if not count_of_digits_even(n):
        dp[(n, x)] = recurse(n*2024, i+1)
        return dp.get((n, x))

    spl = split_num(n)
    dp[(n, x)] = recurse(spl[0], i+1) + recurse(spl[1], i+1) + 1
    return dp.get((n, x))

def solve(nums):
    answer = 0
    for i in range(len(nums)):
        x = recurse(nums[i], 0)
        answer += x
    return answer + len(nums)

with open("input.txt") as file:
    nums = list(map(to_nums, file.readlines()))
    print(solve(nums[0]))
