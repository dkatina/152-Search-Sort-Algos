
#Continuosly split check the center point, and recenter depending if the target is higher or lower

def binary_search(alist, target): #requires a sorted list
    low = 0
    high = len(alist) -1
    while low <= high:
        print("Guess area:", alist[low:high])
        print(low, high)
        mid = (low + high) // 2
        print("Guessing:", alist[mid])
        if alist[mid] == target:
            return f"Found my target at index: {mid}"
        elif target > alist[mid]:
            print("Target is HIGHER, moving low up")
            low = mid + 1
        else: 
            print("Target is LOWER moving high down")
            high = mid -1
    
    return "Target not found"

things = [1,2,3,4,5,6,7,8,9,12,23,34,56,67,78,89,90,123,146,200]
target = 78

print(binary_search(things, target))