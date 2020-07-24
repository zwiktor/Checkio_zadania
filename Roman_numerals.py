# https://py.checkio.org/en/mission/roman-numerals/


def checkio(data):
    result = ''
    num_str = str(data)
    if len(num_str) >= 3:
        num_hundret = num_str[-3]
    if len(num_str) >= 2:
        num_teens = num_str[-2]
    num_num = num_str[-1]

    if data >= 1000:
        result = result + ('M' * int(num_str[0]))
    if data >= 100:
        if int(num_hundret[0]) == 9:
            result = result + 'CM'
        elif int(num_hundret[0]) > 5 and int(num_hundret[0]) < 9:
            divider = int(num_hundret[0])%5
            result = result + 'D' + ('C' * divider)
        elif int(num_hundret[0]) == 5:
            result = result + 'D'
        elif int(num_hundret[0]) == 4:
            result = result + 'CD'
        elif int(num_hundret[0]) >= 1 and int(num_hundret[0]) < 4:
            divider = int(num_hundret[0])%5
            result = result + 'C' * divider

    if data >= 10:
        if int(num_teens[0]) == 9:
            result = result + 'XC'
        elif int(num_teens[0]) > 5 and int(num_teens[0]) < 9:
            divider = int(num_teens[0])%5
            result = result + 'L' + ('X' * divider)
        elif int(num_teens[0]) == 5:
            result = result + 'L'
        elif int(num_teens[0]) == 4:
            result = result + 'XL'
        elif int(num_teens[0]) >= 1 and int(num_teens[0]) < 4:
            divider = int(num_teens[0])%5
            result = result + 'X' * divider
    if data >= 1:
        if int(num_num) == 9:
            result = result + 'IX'
        elif int(num_num) > 5 and int(num_num) < 9:
            divider = int(num_num)%5
            result = result + 'V' + ('I' * divider)
        elif int(num_num) == 5:
            result = result + 'V'
        elif int(num_num) == 4:
            result = result + 'IV'
        elif int(num_num) >= 1 and int(num_num) < 4:
            divider = int(num_num)%5
            result = result + 'I' * divider

    #replace this for solution
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done!')
