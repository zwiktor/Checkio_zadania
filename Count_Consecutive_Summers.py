# https://py.checkio.org/en/mission/count-consecutive-summers/


def count_consecutive_summers(num):
    result = 0
    for start in range(1, num + 1):
        sum_of_numbers = 0
        for number in range(start, num + 1):
            sum_of_numbers += number
            if sum_of_numbers == num:
                result += 1
            elif sum_of_numbers > num:
                break
    return result


if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(42))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding completed")
