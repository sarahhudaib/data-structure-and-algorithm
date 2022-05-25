def partition(input_list, low, high):
    """Function to partition the list   
       Input: input_list, low, high
       Output: partition_index
    """
    i = (low - 1)   # Index of smaller element
    pivot = input_list[high]    # Pivot element is the last element of the list
    for j in range(low, high):  # Loop through the list from the first element to the last element
        if input_list[j] <= pivot:  # If the element is smaller than the pivot element
            i = i + 1   # Increment the index of the smaller element
            # Swap the elements
            input_list[i], input_list[j] = input_list[j], input_list[i]
    # Swap the pivot element with the smaller element
    input_list[i+1], input_list[high] = input_list[high], input_list[i+1]
    return (i+1)    # Return the index of the smaller element


def quick_sort(input_list, low, high):
    """Function to sort the list    
       Input: input_list, low, high
       Output: sorted_list
    """
    if low < high:  # If the list has more than one element
        partition_index = partition(
            input_list, low, high)  # Partition the list
        # Sort the left side of the list
        quick_sort(input_list, low, partition_index - 1)
        # Sort the right side of the list
        quick_sort(input_list, partition_index + 1, high)


if __name__ == "__main__":
    input_l = [9, -3, 5, 2, 6, 8, -6, 1, 3]
    list_length = len(input_l)
    quick_sort(input_l, 0, list_length - 1)

    print(input_l)
