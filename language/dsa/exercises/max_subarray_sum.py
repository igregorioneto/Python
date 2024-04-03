def max_subarray_sum(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(max_subarray_sum(nums, k))