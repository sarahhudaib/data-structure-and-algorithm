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


def test_insert_shift_even():
  actual = insert_shift_array([1, 2, 4, 5], 3)
  expected = [1, 2, 3, 4, 5]
  assert actual == expected


def test_insert_shift_odd():
  actual = insert_shift_array([1, 2, 3, 5, 6], 4)
  expected = [1, 2, 3, 4, 5, 6]
  assert actual == expected