from quick_sort import quick_sort

"""
Reverse-sorted: [20,18,12,8,5,-2]
Few uniques: [5,12,7,5,5,7]
Nearly-sorted: [2,3,5,7,13,11]

"""


def test_few_uniques():
    lst = [100, 1000, 500, 100, 100, 500]
    quick_sort(lst, 0, 5)
    assert lst == [100, 100, 100, 500, 500, 1000]


def test_nearly_sorted():
    lst = [100, 200, 300, 500, 400, 600]
    quick_sort(lst, 0, 5)
    assert lst == [100, 200, 300, 400, 500, 600]


def test_reverse_sorted():
    lst = [20, 18, 12, 8, 5, -2]
    quick_sort(lst, 0, 5)
    assert lst == [-2, 5, 8, 12, 18, 20]


def test_quick_sort():
    lst = [100, 200, 500, 400, 300, 600]
    quick_sort(lst, 0, 5)
    assert lst == [100, 200, 300, 400, 500, 600]


def test_quick_sort_zeros_and_negative():
    lst = [-100, -4, -2, 0, -1]
    quick_sort(lst, 0, 4)
    assert lst == [-100, -4, -2, -1, 0]
