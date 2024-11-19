def maxSum_subArray(k,arr):
    result =0
    start_window = 0
    value =0
    for end_window in range(len(arr)):
        value += arr[end_window]
        if(end_window >= k-1):
            result = max(value, result)
            value -= arr[start_window]
            start_window += 1

    return result
 
def main():
    k=3
    arr = [2, 1, 5, 1, 3, 2]
    result = maxSum_subArray(k,arr)
    print("average sum of subarray is :" , str(result))
    

main()