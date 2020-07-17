'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    return_num = [0 for i in range(len(arr) + 1)]
    for num in arr:
        return_num[num] += 1
        # print(return_num[num])
    for i in range(0, len(return_num)):
        if return_num[i] == 1:
            return i
        # print(i)
    return i

# sean chen lecture
def single_number2(arr):
    s = set()
    for x in arr:
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    return list(s)[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
    print(f"The odd-number-out is {single_number2(arr)}")