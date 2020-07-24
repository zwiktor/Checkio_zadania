# https://py.checkio.org/en/mission/similar-triangles/


def similar_triangles(coords_1, coords_2) -> bool:
    tri_1_side_1 = ((coords_1[1][0] - coords_1[0][0]) ** 2 + (coords_1[1][1] - coords_1[0][1]) ** 2) ** (1 / 2)
    tri_1_side_2 = ((coords_1[2][0] - coords_1[1][0]) ** 2 + (coords_1[2][1] - coords_1[1][1]) ** 2) ** (1 / 2)
    tri_1_side_3 = ((coords_1[0][0] - coords_1[2][0]) ** 2 + (coords_1[0][1] - coords_1[2][1]) ** 2) ** (1 / 2)
    tri_2_side_1 = ((coords_2[1][0] - coords_2[0][0]) ** 2 + (coords_2[1][1] - coords_2[0][1]) ** 2) ** (1 / 2)
    tri_2_side_2 = ((coords_2[2][0] - coords_2[1][0]) ** 2 + (coords_2[2][1] - coords_2[1][1]) ** 2) ** (1 / 2)
    tri_2_side_3 = ((coords_2[0][0] - coords_2[2][0]) ** 2 + (coords_2[0][1] - coords_2[2][1]) ** 2) ** (1 / 2)

    tri_1_sides = [tri_1_side_1, tri_1_side_2, tri_1_side_3]
    tri_1_sides.sort()
    tri_2_sides = [tri_2_side_1, tri_2_side_2, tri_2_side_3]
    tri_2_sides.sort()

    return tri_1_sides[0] / tri_2_sides[0] == tri_1_sides[1] / tri_2_sides[1] == tri_1_sides[2] / tri_2_sides[2]


if __name__ == '__main__':
    print("Example:")
    print(similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    print("Coding completed")
