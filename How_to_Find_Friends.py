# https://py.checkio.org/en/mission/find-friends/


def check_connection(network, drons1, drons2):
    network = [elem.split('-') for elem in network]
    drones = list(set([x for l in network for x in l]))
    drones_connection = []
    for index, dron in enumerate(drones):
        drones_connection.append([])
        for net in network:
            elem1, elem2 = net
            if dron in net:
                drones_connection[index].append(elem1)
                drones_connection[index].append(elem2)

    l = []
    for dron1 in drones_connection:
        dron1 = list(set(dron1))
        for index, dron in enumerate(drones_connection):
            dron = list(set(dron))
            if not index:
                continue
            if set(dron1) & set(dron):
                dron1 = list(set(dron1) | set(dron))
        if dron1 not in l:
            l.append(dron1)
    print(l)
    for connection in l:
        if drons1 in connection and drons2 in connection:
            return True
    return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."

    print('Done!')