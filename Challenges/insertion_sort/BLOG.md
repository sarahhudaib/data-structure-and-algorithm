# Insertion sort

The Insertion sort is a straightforward and more efficient algorithm than the previous bubble sort algorithm. The insertion sort algorithm concept is based on the deck of the card where we sort the playing card according to a particular card. It has many advantages, but there are many efficient algorithms available in the data structure.

While the card-playing, we compare the hands of cards with each other. Most of the player likes to sort the card in the ascending order so they can quickly see which combinations they have at their disposal.


> The insertion sort algorithm is not so fast because of it uses nested loop for sort the elements.
 ----

## What is the meaning of in-place and stable?
- `In-place`: The in-place algorithm requires additional space without caring for the input size of the collection. After performing the sorting, it rewrites the original memory locations of the elements in the collection.

- `Stable`: The stable is a term that manages the relative order of equal objects from the initial array.
The more important thing, the insertion sort doesn't require to know the array size in advance and it receives the one element at a time.

The great thing about the insertion sort is if we insert the more elements to be sorted - the algorithm arranges the in its proper place without performing the complete sort.

It is more efficient for the small (less than 10) size array. Now, let's understand the concepts of insertion sort.

----

## The Concept of Insertion Sort
The array spilled virtually in the two parts in the insertion sort - An unsorted part and sorted part.

The sorted part contains the first element of the array and other unsorted subpart contains the rest of the array. The first element in the unsorted array is compared to the sorted array so that we can place it into a proper sub-array.

It focuses on inserting the elements by moving all elements if the right-side value is smaller than the left side.

> It will repeatedly happen until the all element is inserted at correct place.

To sort the array using insertion sort below is the algorithm of insertion sort.

- Spilt a list in two parts - sorted and unsorted.
- Iterate from arr[1] to arr[n] over the given array.
- Compare the current element to the next element.
- If the current element is smaller than the next element, compare to the element before, Move to the greater elements one position up to make space for the swapped element.

----

## Let's understand the following example.

We will consider the first element in the sorted array in the following array.

```
[10, 4, 25, 1, 5]
```

The first step to add 10 to the sorted subarray

```
[10, 4, 25, 1, 5]
````

Now we take the first element from the unsorted array - 4. We store this value in a new variable temp. Now, we can see that the 10>4 then we move the 10 to the right and that overwrite the 4 that was previously stored.

```
[10, 10, 25, 1, 5] (temp = 4)
```

Here the 4 is lesser than all elements in sorted subarray, so we insert it at the first index position.

```
[4, 10, 25, 1, 5]
```

We have two elements in the sorted subarray.

Now check the number 25. We have saved it into the temp variable. 25> 10 and also 25> 4 then we put it in the third position and add it to the sorted sub array.

```
[4, 10, 25, 1, 5]
```

Again we check the number 1. We save it in temp. 1 is less than the 25. It overwrites the 25.

```
[4, 10, 25, 25, 5] 10>1 then it overwrites again

[4, 25, 10, 25, 5]

[25, 4, 10, 25, 5] 4>1 now put the value of temp = 1

[1, 4, 10, 25, 5]
```

Now, we have 4 elements in the sorted subarray. 5<25 then shift 25 to the right side and pass temp = 5 to the left side.

```
[1, 4, 10, 25, 25] put temp = 5
```

Now, we get the sorted array by simply putting the temp value.

```
[1, 4, 5, 10, 25]
```

The given array is sorted.

----

## Explanation:

In the above code, we have created a function called insertion_sort(list1). Inside the function -

- We defined for loop for traverse the list from 1 to len(list1).
- In for loop, assigned a values of list1 in value Every time the loop will iterate the new value will assign to the value variable.
- Next, we moved the elements of list1[0…i-1], that are greater than the value, to one position ahead of their current position.
- Now, we used the while to check whether the j is greater or equal than 0, and the value is smaller than the first element of the list.
- If both conditions are true then move the first element to the 0th index and reduce the value of j and so on.
- After that, we called the function and passed the list and printed the result.

-----
## Pseudocode

```
 InsertionSort(int[] lst)

    FOR i = 1 to len(lst)

      int j <-- i - 1
      int temp <-- lst[i]

      WHILE j >= 0 AND temp < lst[j]
        lst[j + 1] <-- lst[j]
        j <-- j - 1

      lst[j + 1] <-- temp

```

## Time Complexity in Insertion Sort

Insertion sort is a slow algorithm; sometimes, it seems too slow for extensive dataset. However, it is efficient for small lists or array.

The time complexity of the insertion sort is - O(n2). It uses the two loops for iteration.

Another important advantage of the insertion sort is that; it is used by the popular sorting algorithm called Shell sort.

The auxiliary space in insertion sort: O(1)

---

## Conclusion:
Insertion sort is a simple and inefficient algorithm that has many advantages, but there are more efficient algorithms are available.

In this tutorial, we have discussed the concept of the insertion sort and its implementation using the Python programming language.

----
## Specifics about how it works:

```
Outer Index: 1  CurrentValue:  1        Inner Index: 1

-------->
3       1       0       5       2       9       7       8       6       4
        ↓
        1
sh: 1: cls: not found

Outer Index: 1  CurrentValue:  1        Inner Index: 1

-------->
3       1       0       5       2       9       7       8       6       4
?
        1
sh: 1: cls: not found

Outer Index: 1  CurrentValue:  1        Inner Index: 1

-------->
3------>3       0       5       2       9       7       8       6       4
?
        1
sh: 1: cls: not found

Outer Index: 1  CurrentValue:  1        Inner Index: 0

-------->
3       3       0       5       2       9       7       8       6       4
?
1
sh: 1: cls: not found

Outer Index: 1  CurrentValue:  1        Inner Index: 0

-------->
1       3       0       5       2       9       7       8       6       4
↑
1
Current Index: 2
sh: 1: cls: not found

Outer Index: 2  CurrentValue:  0        Inner Index: 2

---------------->
1       3       0       5       2       9       7       8       6       4
                ↓
                0
sh: 1: cls: not found

Outer Index: 2  CurrentValue:  0        Inner Index: 2

---------------->
1       3       0       5       2       9       7       8       6       4
        ?
                0
sh: 1: cls: not found

Outer Index: 2  CurrentValue:  0        Inner Index: 2

---------------->
1       3------>3       5       2       9       7       8       6       4
        ?
                0
sh: 1: cls: not found

Outer Index: 2  CurrentValue:  0        Inner Index: 1

---------------->
1       3       3       5       2       9       7       8       6       4
?
        0
sh: 1: cls: not found

Outer Index: 2  CurrentValue:  0        Inner Index: 1

---------------->
1------>1       3       5       2       9       7       8       6       4
?
        0
sh: 1: cls: not found

Outer Index: 2  CurrentValue:  0        Inner Index: 0

---------------->
1       1       3       5       2       9       7       8       6       4
?
0
sh: 1: cls: not found

Outer Index: 2  CurrentValue:  0        Inner Index: 0

---------------->
0       1       3       5       2       9       7       8       6       4
↑
0
Current Index: 3
sh: 1: cls: not found

Outer Index: 3  CurrentValue:  5        Inner Index: 3

------------------------>
0       1       3       5       2       9       7       8       6       4
                        ↓
                        5
sh: 1: cls: not found

Outer Index: 3  CurrentValue:  5        Inner Index: 3

------------------------>
0       1       3       5       2       9       7       8       6       4
                ?
                        5
sh: 1: cls: not found

Outer Index: 3  CurrentValue:  5        Inner Index: 3

------------------------>
0       1       3       5       2       9       7       8       6       4
                        ↑
                        5
Current Index: 4
sh: 1: cls: not found

Outer Index: 4  CurrentValue:  2        Inner Index: 4

-------------------------------->
0       1       3       5       2       9       7       8       6       4
                                ↓
                                2
sh: 1: cls: not found

Outer Index: 4  CurrentValue:  2        Inner Index: 4

-------------------------------->
0       1       3       5       2       9       7       8       6       4
                        ?
                                2
sh: 1: cls: not found

Outer Index: 4  CurrentValue:  2        Inner Index: 4

-------------------------------->
0       1       3       5------>5       9       7       8       6       4
                        ?
                                2
sh: 1: cls: not found

Outer Index: 4  CurrentValue:  2        Inner Index: 3

-------------------------------->
0       1       3       5       5       9       7       8       6       4
                ?
                        2
sh: 1: cls: not found

Outer Index: 4  CurrentValue:  2        Inner Index: 3

-------------------------------->
0       1       3------>3       5       9       7       8       6       4
                ?
                        2
sh: 1: cls: not found

Outer Index: 4  CurrentValue:  2        Inner Index: 2

-------------------------------->
0       1       3       3       5       9       7       8       6       4
        ?
                2
sh: 1: cls: not found

Outer Index: 4  CurrentValue:  2        Inner Index: 2

-------------------------------->
0       1       2       3       5       9       7       8       6       4
                ↑
                2
Current Index: 5
sh: 1: cls: not found

Outer Index: 5  CurrentValue:  9        Inner Index: 5

---------------------------------------->
0       1       2       3       5       9       7       8       6       4
                                        ↓
                                        9
sh: 1: cls: not found

Outer Index: 5  CurrentValue:  9        Inner Index: 5

---------------------------------------->
0       1       2       3       5       9       7       8       6       4
                                ?
                                        9
sh: 1: cls: not found

Outer Index: 5  CurrentValue:  9        Inner Index: 5

---------------------------------------->
0       1       2       3       5       9       7       8       6       4
                                        ↑
                                        9
Current Index: 6
sh: 1: cls: not found

Outer Index: 6  CurrentValue:  7        Inner Index: 6

------------------------------------------------>
0       1       2       3       5       9       7       8       6       4
                                                ↓
                                                7
sh: 1: cls: not found

Outer Index: 6  CurrentValue:  7        Inner Index: 6

------------------------------------------------>
0       1       2       3       5       9       7       8       6       4
                                        ?
                                                7
sh: 1: cls: not found

Outer Index: 6  CurrentValue:  7        Inner Index: 6

------------------------------------------------>
0       1       2       3       5       9------>9       8       6       4
                                        ?
                                                7
sh: 1: cls: not found

Outer Index: 6  CurrentValue:  7        Inner Index: 5

------------------------------------------------>
0       1       2       3       5       9       9       8       6       4
                                ?
                                        7
sh: 1: cls: not found

Outer Index: 6  CurrentValue:  7        Inner Index: 5

------------------------------------------------>
0       1       2       3       5       7       9       8       6       4
                                        ↑
                                        7
Current Index: 7
sh: 1: cls: not found

Outer Index: 7  CurrentValue:  8        Inner Index: 7

-------------------------------------------------------->
0       1       2       3       5       7       9       8       6       4
                                                        ↓
                                                        8
sh: 1: cls: not found

Outer Index: 7  CurrentValue:  8        Inner Index: 7

-------------------------------------------------------->
0       1       2       3       5       7       9       8       6       4
                                                ?
                                                        8
sh: 1: cls: not found

Outer Index: 7  CurrentValue:  8        Inner Index: 7

-------------------------------------------------------->
0       1       2       3       5       7       9------>9       6       4
                                                ?
                                                        8
sh: 1: cls: not found

Outer Index: 7  CurrentValue:  8        Inner Index: 6

-------------------------------------------------------->
0       1       2       3       5       7       9       9       6       4
                                        ?
                                                8
sh: 1: cls: not found

Outer Index: 7  CurrentValue:  8        Inner Index: 6

-------------------------------------------------------->
0       1       2       3       5       7       8       9       6       4
                                                ↑
                                                8
Current Index: 8
sh: 1: cls: not found

Outer Index: 8  CurrentValue:  6        Inner Index: 8

---------------------------------------------------------------->
0       1       2       3       5       7       8       9       6       4
                                                                ↓
                                                                6
sh: 1: cls: not found

Outer Index: 8  CurrentValue:  6        Inner Index: 8

---------------------------------------------------------------->
0       1       2       3       5       7       8       9       6       4
                                                        ?
                                                                6
sh: 1: cls: not found

Outer Index: 8  CurrentValue:  6        Inner Index: 8

---------------------------------------------------------------->
0       1       2       3       5       7       8       9------>9       4
                                                        ?
                                                                6
sh: 1: cls: not found

Outer Index: 8  CurrentValue:  6        Inner Index: 7

---------------------------------------------------------------->
0       1       2       3       5       7       8       9       9       4
                                                ?
                                                        6
sh: 1: cls: not found

Outer Index: 8  CurrentValue:  6        Inner Index: 7

---------------------------------------------------------------->
0       1       2       3       5       7       8------>8       9       4
                                                ?
                                                        6
sh: 1: cls: not found

Outer Index: 8  CurrentValue:  6        Inner Index: 6

---------------------------------------------------------------->
0       1       2       3       5       7       8       8       9       4
                                        ?
                                                6
sh: 1: cls: not found

Outer Index: 8  CurrentValue:  6        Inner Index: 6

---------------------------------------------------------------->
0       1       2       3       5       7------>7       8       9       4
                                        ?
                                                6
sh: 1: cls: not found

Outer Index: 8  CurrentValue:  6        Inner Index: 5

---------------------------------------------------------------->
0       1       2       3       5       7       7       8       9       4
                                ?
                                        6
sh: 1: cls: not found

Outer Index: 8  CurrentValue:  6        Inner Index: 5

---------------------------------------------------------------->
0       1       2       3       5       6       7       8       9       4
                                        ↑
                                        6
Current Index: 9
sh: 1: cls: not found

Outer Index: 9  CurrentValue:  4        Inner Index: 9

------------------------------------------------------------------------>
0       1       2       3       5       6       7       8       9       4
                                                                        ↓
                                                                        4
sh: 1: cls: not found

Outer Index: 9  CurrentValue:  4        Inner Index: 9

------------------------------------------------------------------------>
0       1       2       3       5       6       7       8       9       4
                                                                ?
                                                                        4
sh: 1: cls: not found

Outer Index: 9  CurrentValue:  4        Inner Index: 9

------------------------------------------------------------------------>
0       1       2       3       5       6       7       8       9------>9
                                                                ?
                                                                        4
sh: 1: cls: not found

Outer Index: 9  CurrentValue:  4        Inner Index: 8

------------------------------------------------------------------------>
0       1       2       3       5       6       7       8       9       9
                                                        ?
                                                                4
sh: 1: cls: not found

Outer Index: 9  CurrentValue:  4        Inner Index: 8

------------------------------------------------------------------------>
0       1       2       3       5       6       7       8------>8       9
                                                        ?
                                                                4
sh: 1: cls: not found

Outer Index: 9  CurrentValue:  4        Inner Index: 7

------------------------------------------------------------------------>
0       1       2       3       5       6       7       8       8       9
                                                ?
                                                        4
sh: 1: cls: not found

Outer Index: 9  CurrentValue:  4        Inner Index: 7

------------------------------------------------------------------------>
0       1       2       3       5       6       7------>7       8       9
                                                ?
                                                        4
sh: 1: cls: not found

Outer Index: 9  CurrentValue:  4        Inner Index: 6

------------------------------------------------------------------------>
0       1       2       3       5       6       7       7       8       9
                                        ?
                                                4
sh: 1: cls: not found

Outer Index: 9  CurrentValue:  4        Inner Index: 6

------------------------------------------------------------------------>
0       1       2       3       5       6------>6       7       8       9
                                        ?
                                                4
sh: 1: cls: not found

Outer Index: 9  CurrentValue:  4        Inner Index: 5

------------------------------------------------------------------------>
0       1       2       3       5       6       6       7       8       9
                                ?
                                        4
sh: 1: cls: not found

Outer Index: 9  CurrentValue:  4        Inner Index: 5

------------------------------------------------------------------------>
0       1       2       3       5------>5       6       7       8       9
                                ?
                                        4
sh: 1: cls: not found

Outer Index: 9  CurrentValue:  4        Inner Index: 4

------------------------------------------------------------------------>
0       1       2       3       5       5       6       7       8       9
                        ?
                                4
sh: 1: cls: not found

Outer Index: 9  CurrentValue:  4        Inner Index: 4

------------------------------------------------------------------------>
0       1       2       3       4       5       6       7       8       9
                                ↑
                                4
Array Sorted!
0       1       2       3       4       5       6       7       8       9


```
