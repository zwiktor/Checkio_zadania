# https://py.checkio.org/en/mission/verify-anagrams/


def verify_anagrams(first_word, second_word):
    first = first_word.replace(' ', '').lower()
    second = second_word.replace(' ', '').lower()
    for letter in first_word:
        if first.count(letter) != second.count(letter):
            return False
    if len(first) != len(second):
        return False
    return True


print("example")
verify_anagrams("Programming", "Gram Ring Mop")

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"

    print('Done!')