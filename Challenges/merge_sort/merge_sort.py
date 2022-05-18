def merge_sort(lst):
    """function to sort the list using merge sort algorithm
    input: list
    output: sorted list
    """
    elements_count = len(lst)

    if elements_count > 1:
        mid_point = elements_count // 2  # find the midpoint of the list

        left = lst[: mid_point]
        right = lst[mid_point:]

        merge_sort(left)
        merge_sort(right)
        merge(left, right, lst)


def merge(left, right, some_list):
    """ function to merge the left and right sides together using the some_list list
    input: left, right, some_list 
    output: list
    """

    i = 0  # index for left
    j = 0  # index for right
    k = 0  # index for list

    # while there are elements in the left and right lists
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            some_list[k] = left[i]
            i += 1
        else:
            some_list[k] = right[j]
            j += 1

        k += 1

    if i == len(left):  # if there are no more elements in the left list
        for element in right[j:]:
            some_list[k] = element
            k += 1

    else:
        for element in left[i:]:     # for each element in the left list
            some_list[k] = element
            k += 1


if __name__ == "__main__":
    lst = [2, 3, 5, 7, 11, 13]
    merge_sort(lst)
    print("lst", lst)

    lst1 = [1, 1, 1, 1, 1]
    merge_sort(lst1)
    print("lst1", lst1)

    lst2 = [-23, -0.5, -4, 0, -1]
    merge_sort(lst2)
    print("lst2", lst2)
