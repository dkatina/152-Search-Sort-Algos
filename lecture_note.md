# Learning Objectives

- The students should be able to apply linear and binary search algorithms to locate specific elements within a dataset efficiently.
- The students should be able to analyze the time complexity of sorting algorithms, including bubble sort, merge sort, and Timsort, to evaluate their performance in different scenarios.
- The students should be able to implement sorting algorithms, such as bubble sort and merge sort, in Python to organize data structures effectively.
- The students should be able to comprehend practical scenarios where choosing the appropriate search and sorting algorithms is crucial for optimizing efficiency and performance in real-world applications.

### Searching Algorithms

- **Linear Search**: Algorithm goes through each element in the collection, comparing the elements to the target until it either finds a match, or reaches the end of the collection. Linear Search have linear time complexity O(n)

- **Binary Search**: Binary search relies on the list being pre-sorted, and continuously bisecting the list, depending on weather the middle of the list is greater or less than the target.

### Sorting Algorithms
*There are many but here are a few*: https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/visualize/
- **Bubble Sort**: Bubble sort, is a quadratic algo (nested for loops), that makes a pass for every element in the list. With each pass the next largest element gets pushed into it's position.

![bubble](https://media.geeksforgeeks.org/wp-content/uploads/20190704131909/bubblusort.gif)

- **Merge Sort**: Merge sort, requires recursively "breaking down the left side" of a list until your you've broken your list into single unit lists, you then merge these lists single unit lists into double unit lists, then the double unit lists into 4 unit list, so on until your have merged all the pieces together in order. (Reference the Hacker Earth animation). Time complexity is O(n logn)

- **.sort() and sorted()**: The functions are built off of the Timsort algorithm... developed by a guy named Tim. Timsort is a combination of Merge Sort and an algo called Insert Sort and is O(n logn).

#### Configuring your algos

Configuring your algoirthms to search and sort by a specific key is not terrible hard to encode, let's search/ sort through the following'

```python
playlist = [
    {"title": "Terrible", "duration": 180, "upload_date": "2022-01-01"},
    {"title": "awful", "duration": 240, "upload_date": "2021-12-15"},
    {"title": "Pretty Rank", "duration": 200, "upload_date": "2022-01-10"},
]
```