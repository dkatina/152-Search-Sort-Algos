

#Recursively break down until we get to single unit lists
#compare elements in two list continuosly adding the next lowest until a list is empty
#fill in from the non-empty list

def merge_sort(arr): #Time complexity O(n logn)

    if len(arr)> 1:
        mid = len(arr) // 2
        left_side = arr[:mid]
        right_side = arr[mid:]

        #Recursively break down the left side first
        merge_sort(left_side)
        merge_sort(right_side)

        #merge Algo

        i = 0 #main
        j = 0 #left
        k = 0 #right
        
        #Compare and enter data points until a list is empty
        while j < len(left_side) and k < len(right_side):
            if left_side[j] < right_side[k]:
                arr[i] = left_side[j]
                i += 1
                j += 1
            else:
                arr[i] = right_side[k]
                i += 1
                k += 1
        
        #Fill in from the non empty list
        while j < len(left_side): #Left hand side still has data
            arr[i] = left_side[j]
            i+=1
            j+= 1

        while k < len(right_side):
            arr[i] = right_side[k]
            i+=1
            k+=1

alist = [0,1,7,2,3,10,9]

merge_sort(alist)

print(alist)
