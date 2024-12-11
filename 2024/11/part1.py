
def to_nums(s):
    s = s.rstrip()
    s = s.split()
    return [int(x) for x in s]

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

def solve(nums):
    iter_count = 25
    while iter_count > 0:
        l = len(nums)
        i = 0
        while i < l:
            if nums[i] == 0:
                nums[i] = 1
                i += 1
            elif count_of_digits_even(nums[i]):
                spl = split_num(nums[i])
                nums[i] = spl[0]
                nums.insert(i+1, spl[1])
                i += 2
                l += 1
            else:
                nums[i] *= 2024
                i += 1
        iter_count -= 1
    return len(nums)

with open("input.txt") as file:
    nums = list(map(to_nums, file.readlines()))
    print(solve(nums[0]))
