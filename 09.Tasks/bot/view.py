def prints(board):
    cells = ""
    for num, x in enumerate(board):
        cells += " ".join(x)
        if (num+1)%3 == 0:
            cells += "\n"
    return cells