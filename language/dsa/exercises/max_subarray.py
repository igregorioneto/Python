def max_subarray(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    start = 0
    end = k - 1
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        if window_sum > max_sum:
            max_sum = window_sum
            start = i - k + 1
            end = i
    return nums[start:end + 1]

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(max_subarray(nums, k))