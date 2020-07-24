# https://py.checkio.org/en/mission/sort-by-extension/
from typing import List


def sort_by_ext(files: List[str]) -> List[str]:
    full_files = []
    name_files = []
    ext_files = []
    for file in files:
        file = file.split('.')
        if file[-2] == '':
            ext_files.append(file)
        elif file[-1] == '':
            name_files.append(file)
        else:
            full_files.append(file)

    full_files.sort(key=lambda file: file[-1])
    name_files.sort(key=lambda file: file[0])
    ext_files.sort(key=lambda file: file[-1])

    files = ext_files + name_files + full_files
    files_sort = []
    for file in files:
        file = '.'.join(file)
        files_sort.append(file)

    return files_sort


if __name__ == '__main__':
    print("Example:")
    print(sort_by_ext(['.aa.ba', 'aa.', '.ba', '1.cad', '1.bat', '1.aa']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
    print("Coding completed")
