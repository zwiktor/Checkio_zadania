# https://py.checkio.org/en/mission/find-sequence/


def checkio(matrix):
    # HORIZONTAL
    for row in matrix:
        count = 1
        number = row[0]
        for index, num in enumerate(row):
            if index == 0:
                continue
            if num == number:
                count += 1
                if count == 4:
                    return True
            else:
                count = 1
            number = num

    # DIAGONAL
    for col in range(len(matrix[0])):
        count = 0
        col_num = matrix[0][col]
        for row in matrix:
            number = row[col]
            if col_num == number:
                count += 1
                if count == 4:
                    return True
            else:
                count = 1
            col_num = number

    # VERTICAL LEFT-RIGHT
    for row_index, row in enumerate(matrix[:len(matrix) - 3]):
        for num_index, num in enumerate(row[0:len(row) - 3]):
            count = 1
            number = matrix[row_index][num_index]
            next_number = matrix[row_index + 1][num_index + 1]
            if number == next_number:
                count += 1
            while count > 1:
                number = next_number
                next_number = matrix[row_index + count][num_index + count]
                if number == next_number:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 1

    # RETICAL RIGHT-LEFT
    for row_index, row in enumerate(matrix[:len(matrix) - 3]):
        for num_index, num in enumerate(row):
            if num_index > len(row) - 4:
                count = 1
                number = matrix[row_index][num_index]
                next_number = matrix[row_index + 1][num_index - 1]
                if number == next_number:
                    count += 1
                while count > 1:
                    number = next_number
                    next_number = matrix[row_index + count][num_index - count]
                    if number == next_number:
                        count += 1
                        if count == 4:
                            return True
                    else:
                        count = 1

    return False


print(checkio([
    [1, 1, 1, 2],
    [1, 1, 4, 1],
    [1, 3, 1, 6],
    [1, 7, 2, 5]
]))

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"

    print("done!")