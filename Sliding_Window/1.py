def avg_subArray(k,arr):
    start_window = 0
    temp = 0
    result = []
    for end_window in range(len(arr)):
        temp += arr[end_window]
        if(end_window >= k-1):
            result.append(temp/k) 
            temp -= arr[start_window]
            start_window += 1
    return result



def main():
    k=5
    arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    result = avg_subArray(k,arr)
    print("average sum of subarray is :" , str(result))
    

main()