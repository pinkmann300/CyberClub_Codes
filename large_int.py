def large_int(arr):
    index = len(arr) - 1 
    carry = 1 
    while (carry != 0):
        last_val = arr[index] + 1 
        if (last_val == 10) and (index == 0):
            arr[0] = 0 
            arr = [1] + arr
            carry = 0
            break 
        elif (last_val == 10):
            arr[index] = 0 
            index = index - 1 
            carry = 1 
        else:
            arr[index] = last_val 
            break 

    return arr

arr1 = [9]

arr2 = large_int(arr1)
print(arr2)