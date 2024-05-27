import time
arr = [1,5,54,56,1,45,456,786,456,12,75654,4547,4564,13021,76345,4,44]

#Bubble Sort
def bubble_srt(arr):
    count = 0
    comparison = 0
    for i in range(len(arr)):
        swap = False
        for j in range(len(arr)-i-1):
            comparison +=1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
                count +=1
        if not swap: break
    print(f'Number of Bubble Comparisons: {comparison}')
    print(f'Number of Bubble Swaps: {count}')
    return arr
    
#Shout out to Owen for this in his Pathways session. 
start_time = time.time()
sorted_bubble = bubble_srt(arr)
end_time = time.time()
print(f"Algo Time: {end_time - start_time}")
print(sorted_bubble)

#Selection Sort
arr = [1,5,54,56,1,45,456,786,456,12,75654,4547,4564,13021,76345,4,44]
def selection_sort(arr):
    count = 0
    comparison = 0
    for i in range(len(arr)):
        index = i
        comparison += 1
        for j in range(i+1, len(arr)):
            if arr[index] > arr[j]:
               index = j
        if index != i:
            arr[i], arr[index] = arr[index], arr[i]
            count += 1
    
    print(f'Number of Selection Comparisons: {comparison}')
    print(f'Number of Selection Swaps: {count}')
    return arr


start_time = time.time()
sorted_select = selection_sort(arr)
end_time = time.time()
print(f"Algo Time: {end_time - start_time}")
print(sorted_select)



#Insertion Sort
arr = [1,5,54,56,1,45,456,786,456,12,75654,4547,4564,13021,76345,4,44]

def insertion_sort(arr):
    count = 0
    comparisons = 0
    for i in range(1, len(arr)):
        element = arr[i]
        j = i-1
        comparisons +=1
        while j>=0 and element < arr[j]:
            arr[j+1] = arr[j]
            j -=1
            count += 1
        arr[j+1] = element
    print(f'Number of Insertion Comparisons: {comparisons}')
    print(f'Number of Insertion Swaps: {count}')
    return arr

def algo_time(sort_function, arr):
    start_time = time.time()
    sorted_arr, count, comparison = sort_function(arr.copy())
    end_time = time.time()
    elapsed_time = end_time - start_time
    return sorted_arr, count, comparison, elapsed_time

start_time = time.time()
sorted_insert = insertion_sort(arr)
end_time = time.time()
print(f"Algo Time: {end_time - start_time}")
print(sorted_bubble)
