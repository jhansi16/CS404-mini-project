def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

# Take size of the array as input
size = int(input("Enter the size of the array: "))

# Take array elements as input
my_array = []
for _ in range(size):
    element = int(input("Enter an element: "))
    my_array.append(element)

# Perform insertion sort
insertion_sort(my_array)

# Display the sorted array
print("Sorted array:", my_array)
