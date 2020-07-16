'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# def sliding_window_max(nums, k):
#     # Your code here
#     if (len(nums)) == 0 or k == 0:
#         return nums
#     max_arr = []
#     k_window = (len(nums))-k+1
#     i = 0
#     while i < k_window:
#         max_arr.append(max(nums[i:i+k]))
#         i += 1
#     return max_arr

import collections
def sliding_window_max(nums, k):
        win_max = collections.deque()
        max_arr = []
        for i in range(len(nums)):
            while win_max and nums[win_max[-1]] <= nums[i]:
                win_max.pop()
            win_max.append(i)
            if win_max[0] == i - k:
                win_max.popleft()
            if i >= k - 1:
                max_arr.append(nums[win_max[0]])
        return max_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
