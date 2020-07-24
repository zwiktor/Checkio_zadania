# https://py.checkio.org/en/mission/flatten-list/


def flat_list(array_list):
    merged_list = []
    for elem in array_list:
        if type(elem) == type([]):
            merged_list = merged_list + flat_list(elem)
        else:
            merged_list.append(elem)

    return merged_list


if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done!')