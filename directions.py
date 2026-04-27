EMPTY_UNICODE   = "░"
CHANGED_UNICODE = "▒"
FILLED_UNICODE  = "▓"

# COLORS
BLUE = "\033[94m"
GREEN = "\033[92m"
BACKGROUND = "\033[30m"
RESET = "\033[0m"

EMPTY_UNICODE = BACKGROUND + EMPTY_UNICODE + RESET
CHANGED_UNICODE = BLUE + CHANGED_UNICODE + RESET
FILLED_UNICODE = GREEN + FILLED_UNICODE + RESET

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

sorting_directions = {
    "left_right": left_right,
    "right_left": right_left,
    "top_down": top_down,
    "down_top": down_top,
}