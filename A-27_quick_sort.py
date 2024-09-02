def quick_sort(arr):
    iterations = 0
    comparisons = 0
    swaps = 0

    def partition(low, high):
        nonlocal comparisons, swaps
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            comparisons += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
        return i + 1

    def sort(low, high):
        nonlocal iterations
        if low < high:
            iterations += 1
            pi = partition(low, high)
            sort(low, pi - 1)
            sort(pi + 1, high)

    sort(0, len(arr) - 1)
    return arr, iterations, comparisons, swaps

# Example usage
arr = [10, 7, 8, 9, 1, 5]
sorted_arr, iterations, comparisons, swaps = quick_sort(arr)

print("Sorted array:", sorted_arr)
print("Number of iterations:", iterations)
print("Number of comparisons:", comparisons)
print("Number of swaps:", swaps)
