def swap(t, i, j):
    t[i], t[j] = t[j], t[i]
    return i, j

def bubble_sort(t, show_frame):
    n = len(t)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if t[j] > t[j + 1]:
                swap(t, j, j + 1)
                show_frame(t, (j, j + 1))
                
                swapped = True
        if not swapped:
            break
        
def selection_sort(t, show_frame):
    n = len(t)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            show_frame(t, (j, min_index))
            if t[j] < t[min_index]:
                min_index = j
        changed = swap(t, i, min_index)
        show_frame(t, changed)
        
def insertion_sort(t, show_frame):
    n = len(t)
    for i in range(1, n):
        j = i
        while j > 0 and t[j] < t[j - 1]:
            changed = swap(t, j, j - 1)
            j -= 1
            show_frame(t, changed)
def merge(t, render_callback, start, mid, end):
    left_index = start
    right_index = mid + 1

    temp = []
    while left_index <= mid and right_index <= end:
        if t[left_index] <= t[right_index]:
            temp.append(t[left_index])
            left_index += 1
        else:
            temp.append(t[right_index])
            right_index += 1
    # leftovers
    while left_index <= mid:
        temp.append(t[left_index])
        left_index += 1
    while right_index <= end:
        temp.append(t[right_index])
        right_index += 1        



    for i, value in enumerate(temp):
        t[start + i] = value
        render_callback(t, (start + i,))
    

def merge_sort(t, show_frame, start = None, end = None):
    if start is None:
        start = 0
    if end is None:
        end = len(t) - 1

    if start >= end:
        return
    
    mid = (start + end) // 2
    
    merge_sort(t, show_frame, start, mid)
    merge_sort(t, show_frame, mid + 1, end)

    merge(t, show_frame, start, mid, end)

alg_list = {
    "bubble":     bubble_sort,
    "selection":  selection_sort,
    "insertion":  insertion_sort,
    "merge":      merge_sort,
}