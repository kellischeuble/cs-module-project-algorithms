'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    
    # OK I know this is a terrible ~first pass~ solution... but here we go
    numbers = list()
    zeros = list()

    for num in arr:
        if num == 0:
            zeros.append(num)
        else:
            numbers.append(num)

    return numbers + zeros


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")