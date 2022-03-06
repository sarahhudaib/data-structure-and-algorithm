def binary_search(arr, value):
    left = 0
    right = len(arr)
   
    if len(arr) > 0:
        while left <= right:
            mid = (left + right) //2
        
            if arr[mid] == value:
                print(mid)
                return mid
        
            if arr[mid] < value:
                left = mid
            
            if arr[mid] > value:
                right = mid
            if value> len(arr) or value < 0:        
                print('not required')
                return -1

    
if __name__ == '__main__':
    arr= [1, 2, 3, 4, 5, 6, 7, 8]
    value= -10
    print(binary_search(arr,value))  
    
"""
we can use linear search and its gonna be O(n) but its not a good idea because what if we had a list 
of 1 million items and we are looking for the very last element what a bad case!!

i'll take the middle element of the list and ill compare it with the given element
then i'll see if it's bigger or smaller than i'll decide to go left or right upon that comparison 
that will allow me to discard half of the elements which means faster searching.
then i go to middle of the side im standing on (left, right) 
i'll keep repeating the same process until i find my number.

the Big(o) --> 
first iteration n/2 , second iteration = n/2^2 , third iteration =n/2^3  etc.... so iteration x= n/2^x

"""
