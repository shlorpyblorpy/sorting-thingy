import math
import os
import time
import random

EMPTY_UNICODE   = "░░"
CHANGED_UNICODE = "▒▒"
FILLED_UNICODE  = "▓▓"

# COLORS
BLUE = "\033[94m"
GREEN = "\033[92m"
BACKGROUND = "\033[30m"
RESET = "\033[0m"

# SETTING THE COLORS (ONCE)
EMPTY_UNICODE = BACKGROUND + EMPTY_UNICODE + RESET
CHANGED_UNICODE = BLUE + CHANGED_UNICODE + RESET
FILLED_UNICODE = GREEN + FILLED_UNICODE + RESET

MAX_UNICODES_PER_ROW = 5
VISUALIZATION_WAIT_TIME = 0
WATCHING_INTERVAL = 3.1415926

test_table = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8,2,6,4,3]
random.shuffle(test_table)

ROUNDING_TYPES = {
    "floor": math.floor,
    "ceil":  math.ceil,
}

#░ U+2591 LIGHT SHADE (lightly shaded block)
#▒ U+2592 MEDIUM SHADE (medium gray block)
#▓ U+2593 DARK SHADE (dark gray block, the one you asked about)
#█ U+2588 FULL BLOCK (solid black block)

set_rounding = ROUNDING_TYPES["floor"]

# HELPER FUNCTIONS
def reset_cursor():
    print("\033[H\033[J", end="")
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def swap(t, i, j):
    t[i], t[j] = t[j], t[i]
    return i, j
    
def get_sunken_table(t: list):
    biggest_value = max(t)
    if biggest_value == 0:
        return [0] * len(t)
  
    temp = []
    for v in t:
      new_value = set_rounding((v / biggest_value) * MAX_UNICODES_PER_ROW)
      temp.append(new_value)
   
    return temp

# COOLER FUNCTIONS
def left_right(t: list, changed_indices=None):
    biggest = max(t)
  
    for i, v in enumerate(t):
        row = []
        
        for _ in range(v):
            if changed_indices is not None and i in changed_indices:
                row.append(CHANGED_UNICODE)
            else:
                row.append(FILLED_UNICODE)
       
        for _ in range(v, biggest):
            row.append(EMPTY_UNICODE)
       
        print("".join(row))

def right_left(t: list, changed_indices=None):
    biggest = max(t)

    for i, v in enumerate(t):
        row = []
    
        for _ in range(biggest - v):
            row.append(EMPTY_UNICODE)
       
        for _ in range(v):
            if changed_indices is not None and i in changed_indices:
                row.append(CHANGED_UNICODE)
            else:
                row.append(FILLED_UNICODE)
   
        print("".join(row))
 
def top_down(t: list, changed_indices):
    max_height = max(t)
    
    for level in range(1, max_height + 1):
        row = []
        for i, v in enumerate(t):
            if v >= level:
                if changed_indices is not None and i in changed_indices:
                    unicode = CHANGED_UNICODE
                else:
                    unicode = FILLED_UNICODE
            else:
                unicode = EMPTY_UNICODE
            row.append(unicode)
        print("".join(row))

def down_top(t, changed_indices):
    max_height = max(t)
    
    for level in range(max_height, 0, -1):
        row = []
        for i, v in enumerate(t):
            if v >= level:
                if changed_indices is not None and i in changed_indices:
                    unicode = CHANGED_UNICODE
                else:
                    unicode = FILLED_UNICODE
            else:
                unicode = EMPTY_UNICODE
            row.append(unicode)
        print("".join(row))

# COOL TABLE

sorting_orders = {
    "left_right": left_right,
    "right_left": right_left,
    "top_down": top_down,
    "down_top": down_top,
}

# EXTREMELY COOL FUNCTIONS

def visualize(t, order, algorithm):
    clear_screen()
    
    print(f"alg: {str(algorithm.__name__)}\ndir: {order.__name__}")
    time.sleep(WATCHING_INTERVAL)
    clear_screen()
    
    def render_frame(t, changed_indices=None):
        reset_cursor()
        sunken_table = get_sunken_table(t)
        
        buffer = []
        def capture_print(line):
            buffer.append(line)
        
        original_print = print
        try:
            globals()['print'] = lambda *args, **kwargs: capture_print(" ".join(map(str, args)))
            order(sunken_table, changed_indices)
        finally:
            globals()['print'] = original_print
        
        print("\n".join(buffer))
        time.sleep(VISUALIZATION_WAIT_TIME)
    algorithm(t, render_frame)
    
    time.sleep(WATCHING_INTERVAL)
    # TODO: finishing animation
    
# SORTING ALGS

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
        
algorithms = {
    "bubble":     bubble_sort,
    "selection":  selection_sort,
    "insertion":  insertion_sort,
}

visualize(test_table, sorting_orders["down_top"], algorithms["selection"])
