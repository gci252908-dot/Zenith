letters = ["A","B","C","D","E","F","G"]
cur = -1
next_letter = None

def get_next_letter():
    global cur
    cur += 1
    next_letter = letters[cur]
    return next_letter

def reset():
    global cur
    cur = -1