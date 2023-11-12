def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        # Find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Take size of the array as input
size = int(input("Enter the size of the array: "))

# Take array elements as input
my_array = []
for _ in range(size):
    element = int(input("Enter an element: "))
    my_array.append(element)

# Perform selection sort
selection_sort(my_array)

# Display the sorted array
print("Sorted array:", my_array)
