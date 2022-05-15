from insertion_sort import insertion_sort

"""
Reverse-sorted: [20,18,12,8,5,-2]
Few uniques: [5,12,7,5,5,7]
Nearly-sorted: [2,3,5,7,13,11]
"""
def test_list_reverse_sorted():
    some_list = [20,18,12,8,5,-2]
    insertion_sort(some_list)
    assert some_list == [-2, 5, 8, 12, 18, 20]
    
def test_lest_few_uniques():
    some_list = [5,12,7,5,5,7]
    insertion_sort(some_list)
    assert some_list == [5, 5, 5, 7, 7, 12]
    
def test_lest_nearly_sorted():
    some_list = [2,3,5,7,13,11]
    insertion_sort(some_list)
    assert some_list == [2, 3, 5, 7, 11, 13]

def test_list_edge_case_zeros_ones():
    some_list = [-23, -0.5, -4, 0, -1]
    insertion_sort(some_list)
    assert some_list == [-23, -4, -1, -0.5, 0]






    
    
