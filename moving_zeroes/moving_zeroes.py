'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    moved_arr = []
    for element in arr:
        if element != 0:
            moved_arr.insert(0, element)
        else:
            moved_arr.append(element)

    return moved_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")