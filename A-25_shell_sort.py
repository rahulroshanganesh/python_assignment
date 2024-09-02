def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    iterations = 0
    comparisons = 0
    swaps = 0

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            iterations += 1

            while j >= gap and arr[j - gap] > temp:
                comparisons += 1
                arr[j] = arr[j - gap]
                j -= gap
                swaps += 1

            arr[j] = temp
            if j >= gap:
                comparisons += 1

        gap //= 2

    return arr, iterations, comparisons, swaps

# Example usage
arr = [12, 34, 54, 2, 3]
sorted_arr, iterations, comparisons, swaps = shell_sort(arr)

print("Sorted array:", sorted_arr)
print("Number of iterations:", iterations)
print("Number of comparisons:", comparisons)
print("Number of swaps:", swaps)
