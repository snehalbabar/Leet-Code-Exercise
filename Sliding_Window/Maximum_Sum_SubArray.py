def max_sum_subArray(k,arr):
    max_sum = 0
    start_window =0
    window_sum = 0.0
    for end_window in range(len(arr)):
        window_sum += arr[end_window]
        if end_window >= k-1:
            max_sum = max(max_sum,window_sum)
            window_sum -= arr[start_window]
            start_window += 1

    return max_sum

def main():
    k=2
    arr = [2, 3, 4, 1, 5]
    result = max_sum_subArray(k,arr)
    print("average sum of subarray is :" , str(result))
    

main()