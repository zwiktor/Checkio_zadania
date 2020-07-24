# https://py.checkio.org/en/mission/mathematically-lucky-tickets/


def combine(x, y):
    return [x+y, x-y, x*y] + ([x/y] if y != 0 else [])


def checkio(data):
    N = len(data)
    gen = {}
    for l in range(1,N+1):
        for i in range(0,N+1-l):
            gen[i, l] = set([int(data[i:i+l])])
            for k in range(1, l):
                gen[i, l] |= set(g for x in gen[i,k] for y in gen[i+k,l-k]
                                   for g in combine(x, y))
    return 100 not in gen[0, N]


if __name__ == '__main__':
    assert checkio('000000') == True, "All zeros"
    assert checkio('707409') == True, "You can not transform it to 100"
    assert checkio('595347') == False, "(5 + ((9 / (3 / 34)) - 7)) = 100"
    assert checkio('271353') == False, "(2 - (7 * (((1 / 3) - 5) * 3))) = 100"

    print('Done!')