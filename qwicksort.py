#python code for implementation fo quick sort algorithm

def quicksort(arr,left,right):                                  #function for dividing the main array for sorting 
    if left < right:
        partition_pos = partition(arr,left,right)                
        quicksort(arr,left,partition_pos-1)                     
        quicksort(arr,partition_pos+1,right)                    

def partition(arr,left,right):                                  #function for sorting the array recursively
    i = left                                                    
    j = right-1                                                 
    pivot = arr[right]                                          #the pivot element(the last element of the array) 
    
    while i < j:                                                # i index will move foreward
        while i < right and arr[i] < pivot:                     
            i+=1
        while j > left and arr[j] >= pivot:                     # j index will move backward
            j-=1
        if i < j:                                            
            arr[i],arr[j] = arr[j],arr[i]                       # swapping the element

    if arr[i] > pivot: 
        arr[i],arr[right] = arr[right],arr[i]                   # swapping the element if i element is greater than pivot element 

    return i    

#                              predefined array (first type of value input)
my_arr=[]                                                        
my_arr=[int(x) for x in input("Enter the unsorted array: ").split()]            #taking user input for array  
print(my_arr)
quicksort(my_arr,0,len(my_arr)-1)                               #function call
print("The sorted elements are: " , my_arr)