letters = ["A","B","C","D","E","F","G"]
cur = -1
next_letter = None

def get_next_letter():
    """ Grabs the next letter available as an option """
    global cur
    cur += 1
    next_letter = letters[cur]
    return next_letter

def reset():
    """ Resets back to letter A """
    global cur
    cur = -1