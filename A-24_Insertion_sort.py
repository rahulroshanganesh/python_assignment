"""
 Insertion Sort
Implement Insertion Sort in Python
Print the following:
• Number of iterations.
• Number of comparisons
• Number of swaps

"""
def insertion_sort(arr):
    iterations = 0
    comparisons = 0
    swaps = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        iterations += 1

        while j >= 0 and key < arr[j]:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
            swaps += 1

        arr[j + 1] = key
        if j >= 0:
            comparisons += 1

    return arr, iterations, comparisons, swaps

# Example usage
arr = [12, 11, 13, 5, 6]
sorted_arr, iterations, comparisons, swaps = insertion_sort(arr)

print("Sorted array:", sorted_arr)
print("Number of iterations:", iterations)
print("Number of comparisons:", comparisons)
print("Number of swaps:", swaps)
