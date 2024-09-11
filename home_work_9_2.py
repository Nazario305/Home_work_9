def difference(*nums):
    if len(nums) == 0:
        return 0
    else:
        nin_nums = min(nums)
        max_nums = max(nums)
        result = max_nums - nin_nums
    # print(round(result, 2))
    return round(result, 2)

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
