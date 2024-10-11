def avg_subArray(k, arr):
    res = []
    for i in range(len(arr)-k+1):
        sum =0.0
        for j in range(i,i+k):
            sum += arr[j]
        res.append(sum/k)
    return res


def main():
    k=5
    arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    result = avg_subArray(k,arr)
    print("average sum of subarray is :" , str(result))
    

main()