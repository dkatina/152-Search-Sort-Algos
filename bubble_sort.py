
#Bubble sort:
#: Making a pass for every element in the list
#: During each pass we compare all elements
#: End each pass by placing the "next largets" element

def bubble_sort(arr):

    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            print(f"Checking if {arr[j]} > {arr[j+1]}")
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print("Swapping")
            print(arr)
        print(f"Pass {i+1} complete")
    

lst = [34,21,65,234,456,123,1]
bubble_sort(lst)

print(lst)