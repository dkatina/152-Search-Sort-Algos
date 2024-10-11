# The objective of this assignment is to create a recursive function that will 
# continuously open and search through folders until it finds the target file 
# (the target may not exist). To start you will be given a list that represents 
# your systems file system, within this file system will be lists that represent 
# folder, and strings that represent files. Each folder has the potential to hold 
# more folders which could all contain our target file, so we need to be diligent 
# about searching through each one of our folders no matter how deep into our file 
# system we are. Once you have found your target print a "big HOORAY"

file_system = [
    [
        "nothing.txt",
        "dog_pic.png",
        [
            "secret_plan.pdf"
        ]
    ],
    "notion.app",
    "slack.app",
    [
        "fun.txt",
        [
            "meaningless_file.txt",
            "chicken_dinner.txt"
        ],
        "not_fun.txt"
    ],
    "zoom.app"
]

target = "dinner.txt"


#write a func that takes in a fs and a target
#go through each item in the filestructure
#if the item is a file, see if its our target
#--- return Hooray if it is
#if our item is a folder(list) recursively call our func on that folder
# -- wait for the response
# check if that response found the folder
# if so return Hooray
# if not continue searching through the current file
# until there is nothing left to search.

basic = [
    "a_file.txt",
    [
        "b_file.txt"
    ],
    "c_file.txt"
]


def find_file(file_system, target):

    for item in file_system:
        if item == target:
            return "HOORAY"
        elif isinstance(item, list):
            response = find_file(item, target)
            if response == "HOORAY":
                return response
            
    return "File Not Found"

print(find_file(file_system, target))
