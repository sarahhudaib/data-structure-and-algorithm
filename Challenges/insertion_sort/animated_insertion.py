import random,time,os

l = [i for i in range(10)]
random.shuffle(l)

def redraw(arrow = "↑",shift=0,moved_right=False):
    os.system('cls')
    print()
    print("Outer Index:",index, "\tCurrentValue: ",currentValue, "\tInner Index:",currentPosition)
    print()
    print("--------"*index+">")
    if not moved_right:
        for item in l: print(str(item) + "\t",end = "")
    else:
        for item in l[0:currentPosition-1]: print(str(item) + "\t",end = "")
        print(l[currentPosition],end="")
        print("------>",end="")
        for item in l[currentPosition:]: print(str(item) + "\t",end = "")
    print()
    print("\t"*(currentPosition+shift)+arrow)
    print("\t"*(currentPosition)+str(currentValue))
    time.sleep(2)


def insertion_sort(array):
    global index,currentPosition,currentValue,l
    for index in range(1, len(array)):
        print("Current Index:",index)
        currentValue = array[index]
        currentPosition = index
        
        redraw(arrow ="↓")
        
        
        redraw(arrow ="?",shift =-1)
        while currentPosition > 0 and array[currentPosition - 1] > currentValue:
            array[currentPosition] = array[currentPosition -1]
            redraw(arrow ="?",shift =-1,moved_right=True)
            currentPosition = currentPosition - 1
            redraw(arrow ="?",shift =-1)
            
        
        array[currentPosition] = currentValue
        
        redraw()
        

        
insertion_sort(l)

print("Array Sorted!")
for item in l: print(str(item) + "\t",end = "")
input()