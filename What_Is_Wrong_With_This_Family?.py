# https://py.checkio.org/en/mission/wrong-family/


def is_family(tree):
    list_family = list(set([con[0] for con in tree] + [con[1] for con in tree]))
    family_tree = [tree[0][0]]
    repeat = 0
    for con in tree:
        if con[0] in family_tree:
            repeat = 0
            family_tree.insert(family_tree.index(con[0]) + 1, con[1])
        elif con[1] in family_tree and family_tree.index(con[1]) == 0:
            repeat = 0
            family_tree.insert(family_tree.index(con[1]), con[0])
        else:
            if con is not tree[-1] and repeat <= len(family_tree):
                repeat += 1
                tree.append(con)

    return len(list_family) == len(family_tree)


print(is_family([
    ['Logan', 'Mike'],
    ['Logan', 'Jack'],
    ['Jack', 'Alexander']
]))

if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_family([
        ['Logan', 'Mike']
    ]) == True, 'One father, one son'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack']
    ]) == True, 'Two sons'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Alexander']
    ]) == True, 'Grandfather'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Logan']
    ]) == False, 'Can you be a father to your father?'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Jack']
    ]) == False, 'Can you be a father to your brother?'
    assert is_family([
        ['Logan', 'William'],
        ['Logan', 'Jack'],
        ['Mike', 'Alexander']
    ]) == False, 'Looks like Mike is stranger in Logan\'s family'
    print("Done!")
