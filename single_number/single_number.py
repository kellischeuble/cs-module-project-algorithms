'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):

    repeats = list()
    
    for i, num in enumerate(arr):
        if not num in arr[i+1:] and not num in repeats:
            return num
        repeats.append(num)

    # First solution:
    # Looks like this doesn't work because 
    # the test randomized it so that they won't always
    # be next to each other

    # double = True
    # i = 0

    # while double == True:
    #     if arr[i] != arr[i+1]:
    #         double = False
    #         odd_out = arr[i]
    #     i += 2

    # return odd_out

    # TODO: 
    # Recursive implementation

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")