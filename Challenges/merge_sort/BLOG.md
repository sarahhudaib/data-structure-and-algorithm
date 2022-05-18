# Merge Sort

Merge sort is similar to the quick sort algorithm as works on the concept of divide and conquer. It is one of the most popular and efficient sorting algorithm. It is the best example for divide and conquer category of algorithms.

It divides the given list in the two halves, calls itself for the two halves and then merges the two sorted halves. We define the merge() function used to merging two halves.

The sub lists are divided again and again into halves until we get the only one element each. Then we combine the pair of one element lists into two element lists, sorting them in the process. The sorted two element pairs is merged into the four element lists, and so on until we get the sorted list.

----

## Merge Sort Concept

Let's see the following Merge sort diagram.

We have divided the given list in the two halves. The list couldn't be divided in equal parts it doesn't matter at all.

Merge sort can be implement using the two ways - top-down approach and bottom-up approach. We use the top down approach in the above example, which is Merge sort most often used.

The bottom-up approach provides the more optimization which we will define later.

The main part of the algorithm is that how we combine the two sorted sublists. Let's merge the two sorted merge list.

```
A : [2, 4, 7, 8]
B : [1, 3, 11]
sorted : empty
```
First, we observe the first element of both lists. We find the B's first element is smaller, so we add this in our sorted list and move forward in the B list.

```
A : [2, 4, 7, 8]
B : [1, 3, 11]
Sorted : 1
```

Now we look at the next pair of elements 2 and 3. 2 is smaller so we add it into our sorted list and move forward to the list.

```
A : [2, 4, 7, 8]
B : [1, 3, 11]
Sorted : 1
```

Continue this process and we end up with the sorted list of {1, 2, 3, 4, 7, 8, 11}. There can be two special cases.

What if both sublists have same elements - In such case, we can move either one sublist and add the element to the sorted list. Technically, we can move forward in both sublist and add the elements to the sorted list.

We have no element left in one sublist. When we run out the in a sublist simply add the element of the second one after the other.
We should remember that we can sort the element in the any order. We sort the given list in ascending order but we can easily sort in descending order.

----

## Implementation
The merge sort algorithm is implemented by suing the top-down approach. It can be look slightly difficult, so we will elaborate each step in details. Here, we will implement this algorithm on two types of collections - integer element's list (typically used to introduce sorting) and a custom objects (a more practical and realistic scenario).

----
## Pseudo Code

```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```
----

## Sorting Array
The main concept of algorithm is to divide (sub)list into halves and sort them recursively. We continue the process until we end up lists that have only one element. Let's understand the following function for division -

```
def merge_sort(array, left_index, right_index):   
       if left_index >= right_index:   
                 return middle = (left_index + right_index)//2   
       merge_sort(array, left_index, middle)   
       merge_sort(array, middle + 1, right_index)   
       merge(array, left_index, right_index, middle)   
```

Our primary focus to divide the list into subparts before the sorting happen. We need to get the integer value so we use the // operator for our indices.

Let's understand the above procedure by following steps.

- First step is to create copies of lists. The first list contains the lists from [left_index,...,middle] and the second from [middle+1,?,right_index].
- We traverse both copies of list by using the pointer, select the smaller value of the two values and add them to the sorted list. Once we add the element to the list and we move forward in the sorted list regardless.
- Add the remaining elements in the other copy to the sorted array.

-----

## Merge sort complexity
- Time Complexity
```
Worst Case Complexity: O(n*log n)
```

- Space Complexity
```
The space complexity of merge sort is O(n).
```
-----

## Conclusion
Merge Sort works both with a large and small number of elements making it more efficient than Bubble, Insertion and Selection Sort. This comes at a price since Merge Sort uses additional space to produce a sorted list.