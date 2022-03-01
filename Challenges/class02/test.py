# odd number test len 7
# list = [1, 2, 3, 4, 6, 7, 8] 
# value = 5

# even number test len 6
list = [1, 2, 3, 4, 6, 7] 
value = 5
def insert_shift_array(array , value):
    # for 7 items, after the 4th
    midpoint = len(array)//2    
    array = array[0:midpoint] + [value] + array[midpoint:] 
    # => [1, 2, 3, 4, 5, 7, 8, 9]
    print (array) 
    

print(insert_shift_array(list,value))