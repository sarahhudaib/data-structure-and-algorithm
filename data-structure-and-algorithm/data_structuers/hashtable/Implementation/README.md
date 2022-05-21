# Implementation: Hash Tables.
Author: Sarah Hudaib


## Challenge / API
Implement a Hashtable with the following methods:

- Class hashTable() with init that takes (size & data)
-	set
    -	Arguments: key, value
    -	Returns: nothing
    -	This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
    -	Should a given key already exist, replace its value from the value argument given to this method.
-	get
    -	Arguments: key
    -	Returns: Value associated with that key in the table
-	contains
    -	Arguments: key
    -	Returns: Boolean, indicating if the key exists in the table already.
-	keys
    -	Returns: Collection of keys
-	hash
    -	Arguments: key
    -	Returns: Index in the collection for that key


## Approach & Efficiency
-	set(self, key, value) 
-	get(self, key) 
-	contains(self, key)
-	keys(self) 
-	hash(self, key) 

> Big O(1) for the time & space complexity except for the hash method which is O(n) for the time complexity.
 

## Tests
[Link](./test_hashtable.py) 

## Code
[Link](./hashtable.py) 