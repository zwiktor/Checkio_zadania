# https://py.checkio.org/en/mission/pawn-brotherhood/


def safe_pawns(pawns: set) -> int:
    pawns = list(pawns)
    table_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    covered_pawns = 0

    for i in pawns:
        letter = i[0]
        number = i[1]
        covers = []

        if 7 > table_letter.index(letter) > 0:
            covers.append(table_letter[table_letter.index(letter) - 1] + str(int(number) - 1))
            covers.append(table_letter[table_letter.index(letter) + 1] + str(int(number) - 1))
        elif table_letter.index(letter) == 7:
            covers.append(table_letter[table_letter.index(letter) - 1] + str(int(number) - 1))
        elif table_letter.index(letter) == 0:
            covers.append(table_letter[table_letter.index(letter) + 1] + str(int(number) - 1))

        for cov in covers:
            if cov in pawns:
                covered_pawns += 1
                break

    return covered_pawns


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding completed")
