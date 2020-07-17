'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    moved_arr = [] # create empty array
    for element in arr:
        if element != 0:
            # moved_arr.insert(0, element)
            moved_arr = [element] + moved_arr # add to array
        else:
            moved_arr.append(element) # add zeros to end

    return moved_arr

# other option

def moving_zeroes2(arr):
    i = j = 0
    for i in range(0, len(arr)):
        if arr[i] !=0:
            arr[j], arr[i] = arr[i], arr[j]
            j+=1
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
    print(f"The resulting of moving_zeroes is: {moving_zeroes2(arr)}")