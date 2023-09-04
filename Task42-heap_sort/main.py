from random import randint

def heapify(nums, heap_size, index):
    largest = index
    left_child = (2 * index) + 1
    right_child = (2 * index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != index:
        nums[index], nums[largest] = nums[largest], nums[index]
        heapify(nums, heap_size, largest)

def heap_sort(array_nums):
    length = len(array_nums)
    
    for i in range(length, -1, -1):
        heapify(array_nums, length, i)

    for i in range(length - 1, 0, -1):
        array_nums[i], array_nums[0] = array_nums[0], array_nums[i]
        heapify(array_nums, i, 0)

array = [randint(0,50) for i in range(10)]
print(array)
heap_sort(array)
print(array)