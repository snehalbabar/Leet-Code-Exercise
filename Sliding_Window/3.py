import math

def smallest_subArray(s,arr):
    window_start =0
    window_min = math.inf
    value = 0
    for window_end in range(len(arr)):
        #add elements until sum become greater or equal to s
        value += arr[window_end]
        while(value >= s):
            window_min = min(window_min,(window_end - window_start)+1)
            value -= arr[window_start]
            window_start += 1
    return window_min

def main():
    s=7
    arr = [2, 1, 5, 2, 3,2]
    result = smallest_subArray(s,arr)
    print("average sum of subarray is :" , str(result))
    

main()