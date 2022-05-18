def insertion_sort(some_list):
    """This function sorts a list using the insertion sort algorithm.
    input: some_list, a list of integers
    output: a sorted list of integers

    """
    for outer_index in range(1, len(some_list)):

        inner_index = outer_index - 1  # inner_index is the index of the previous element
        # current_element is the element to be inserted
        current_element = some_list[outer_index]

        while inner_index >= 0 and current_element < some_list[inner_index]:
            # while the element to be inserted is less than the previous element and the index is greater than 0
            # shift the previous element to the right
            some_list[inner_index + 1] = some_list[inner_index]
            inner_index = inner_index - 1

        # insert the element to be inserted
        some_list[inner_index+1] = current_element


if __name__ == "__main__":
    lst = [42, 23, 16, 15, 8, 4]
    insertion_sort(lst)
    print("list", lst)

    lst1 = [20, 18, 12, 8, 5, -2]
    insertion_sort(lst1)
    print("lst1", lst1)

    lst2 = [-23, -0.5, -4, 0, -1]
    insertion_sort(lst2)
    print("list2", lst2)

    lst3 = [5, 12, 7, 5, 5, 7]
    insertion_sort(lst3)
    print("list3", lst3)

    lst4 = [2, 3, 5, 7, 13, 11]
    insertion_sort(lst4)
    print("list4", lst4)

    lst5 = [2, 3, 5, 7, 11, 13]
    insertion_sort(lst5)
    print("list5", lst5)

    lst6 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    insertion_sort(lst6)
    print("list6", lst6)
