def avg_subArray(k,arr):
    res = []
    startWindow, windowSum = 0,0.0
    for endWindow in range(len(arr)):
        windowSum += arr[endWindow]
        if(endWindow >= k-1):
            res.append(windowSum/k)
            windowSum -= arr[startWindow]
            startWindow += 1

    return res
    

def main():
    k=5
    arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    result = avg_subArray(k,arr)
    print("average sum of subarray is :" , str(result))
    

main()