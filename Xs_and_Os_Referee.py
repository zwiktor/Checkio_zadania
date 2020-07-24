# https://py.checkio.org/en/mission/x-o-referee/
from typing import List

"""
wyciągnąć indexy 
gdy 3 cyfry są podzielne przez 3,3 i reszta 1, 3 i reszta 2 pionowo
gdy znaki o indexach [0:3], [3:6], [6:9] są takie same poziomo
gdy indexy podzielne przez 4 skos nw-se
gdy indexy podzielne przez 2 bez dwóch pierwszych i ostatnich elementów
"""


def checkio(game_result: List[str]) -> str:
    x_indexes = []
    o_indexes = []
    string = ""
    for i in game_result:
        string += i

    for index, i in enumerate(string):
        if i == "X":
            x_indexes.append(index)
        elif i == "O":
            o_indexes.append(index)

    first_col_x = 0
    second_col_x = 0
    third_col_x = 0
    for x in x_indexes:
        x += 3
        if x % 3 == 0:
            first_col_x += 1
        elif x % 3 == 1:
            second_col_x += 1
        elif x % 3 == 2:
            third_col_x += 1
    if first_col_x >= 3 or second_col_x >= 3 or third_col_x >= 3:
        return "X"
    elif string[0:3] == "XXX" or string[6:9] == "XXX" or string[3:6] == "XXX":
        return "X"
    elif string[2] == "X" and string[4] == "X" and string[6] == "X":
        return "X"
    elif string[0] == "X" and string[4] == "X" and string[8] == "X":
        return "X"

    first_col_o = 0
    second_col_o = 0
    third_col_o = 0
    for o in o_indexes:
        o += 3
        if o % 3 == 0:
            first_col_o += 1
        elif o % 3 == 1:
            second_col_o += 1
        elif o % 3 == 2:
            third_col_o += 1
    if first_col_o >= 3 or second_col_o >= 3 or third_col_o >= 3:
        return "O"
    elif string[0:3] == "OOO" or string[6:9] == "OOO" or string[3:6] == "OOO":
        return "O"
    elif string[2] == "O" and string[4] == "O" and string[6] == "O":
        return "O"
    elif string[0] == "O" and string[4] == "O" and string[8] == "O":
        return "O"

    return "D"


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding completed")