import math
import os
import time
import random
from algorithms import alg_list
from directions import sorting_directions

MAX_UNICODES_PER_ROW = 0
VISUALIZATION_WAIT_TIME = 0.01
WATCHING_INTERVAL = 3.1415926
AUTO_SCALE = True

test_table = [1,2,3,4,5,6,7,8,9,9,9,6,5,3,2,3,4,6,8,9,10,30,0]
random.shuffle(test_table)

ROUNDING_TYPES = {
    "floor": math.floor,
    "ceil":  math.ceil,
}

set_rounding = ROUNDING_TYPES["floor"]

# HELPER FUNCTIONS
def reset_cursor():
    print("\033[H\033[J", end="")
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_sunken_table(t: list):
    biggest_value = max(t)
    if biggest_value == 0:
        return [0] * len(t)

    if AUTO_SCALE:
        size = os.get_terminal_size()
        
        max_height = size.lines - 3
        max_width  = size.columns

        scaled = [
            set_rounding((v / biggest_value) * max_height)
            for v in t
        ]

        if len(scaled) > max_width:
            factor = len(scaled) / max_width
            compressed = []

            for i in range(max_width):
                index = int(i * factor)
                compressed.append(scaled[index])

            return compressed

        return scaled

    else:
        max_height = MAX_UNICODES_PER_ROW
        return [
            set_rounding((v / biggest_value) * max_height)
            for v in t
        ]

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

        
visualize(test_table.copy(), sorting_directions["down_top"], alg_list["merge"])
