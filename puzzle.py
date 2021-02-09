'''
Puzzle game
https://github.com/elem3ntary/puzzle
'''


def validate_board(board):
    '''
    Checks all validation rules on board
    '''
    rules = [check_rows, check_cols, check_blocks]
    for rule in rules:
        if not rule(board):
            return False
    return True


def check_uniqueness(list_to_check):
    '''
    Checks if values in list are unique
    '''
    return len(set(list_to_check)) == len(list_to_check)


def check_range(str_to_check):
    '''
    Checks if numbers in list are in required range
    '''
    if str_to_check.strip() == '':
        return True
    list_to_check = list(map(int, list(str_to_check)))
    if max(list_to_check) <= 9 and min(list_to_check) >= 1:
        return True
    return False


def check_rows(board):
    '''
    Checks rows for validity
    '''
    for row in board:
        row = row.replace('*', '')
        row = row.replace(' ', '')
        if not check_uniqueness(row) or not check_range(row):
            return False
    return True


def check_cols(board):
    '''
    Converts cols to rows and checks for validity
    '''
    columns = []
    for i in range(9):
        column = []
        for row in board:
            column.append(row[i])
        columns.append(''.join(column))
    return check_rows(columns)


def check_blocks(board):
    '''
    Converts color blocks to rows and checks for validity
    '''
    blocks = []
    for i in range(5):
        block = []
        start_idx = 4 - i
        for b in range(5):
            block.append(board[b+i][start_idx])
            if b == 4:
                for c in range(4):
                    block.append(board[b+i][start_idx+c])
        blocks.append(''.join(block))
    return check_rows(blocks)


# if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    # board = [
    #     "**** ****",
    #     "***1 ****",
    #     "**  3****",
    #     "* 4 1****",
    #     "     9 5 ",
    #     " 6  83  *",
    #     "3   1  **",
    #     "  8  2***",
    #     "  2  ****"
    # ]
    # # print(check_blocks(board))
    # print(validate_board(board))
