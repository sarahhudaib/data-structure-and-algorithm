# Hashmap Left Join
Author: Sarah Hudaib


## Challenge / API
Write a function that LEFT JOINs two hashmaps into a single data structure.

- `Arguments`: two hash maps
- `The first parameter` is a hashmap that has word strings as keys, and a synonym of the key as values.
- `The second parameter` is a hashmap that has word strings as keys, and antonyms of the key as values.
- `Return`: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic

## NOTES:

- Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.
- `LEFT JOIN` means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row.
- If no values exist in the right hashmap, then some flavor of `NULL` should be appended to the result row.

## Approach & Efficiency
- def left_join(h1,h2) -> I am assuming h1 and h2 are dictionaries


> Big O(n) for the time & space complexity except for the hash method which is O(n) for the time complexity.
 
## Whiteboard Process
![alt text](./left_join.jpg "left_join")

## Tests
[Link](./test_left_join.py) 

## Code
[Link](./left_join.py) 