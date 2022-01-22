def max_sub_array_of_size_k(k, arr):
    arrayStart, currentSum, maxSum = 0, 0, 0

    for i in range(len(arr)):
        currentSum += arr[i]

        if i >= k - 1:
            maxSum = currentSum if currentSum > maxSum else maxSum
            currentSum -= arr[arrayStart]
            arrayStart += 1

    return maxSum
