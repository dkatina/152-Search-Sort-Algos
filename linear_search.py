
#linear search: checking every item in the collection for my target

def search(alist, target):
    count = 1
    for item in alist:
        print(f"Check if {item} == {target}")
        if item == target:
            return f"Found Target after {count} tries."
        print("It was not gotta try again!")
        count += 1

    return "Target not found!"

alist = [1,2,3,4,5,6,723,45,67,89,122,234,578]
target = 723

print(search(alist, target))