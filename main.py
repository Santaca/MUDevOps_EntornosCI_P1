"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
DEFAULT_ORDER = True

def sort_list(items, ascending):
    if not isinstance(items, list):
        raise RuntimeError(f"The items can't be sorted {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    sortOrder = sys.argv[3] if len(sys.argv) == 4 else DEFAULT_ORDER
    if len(sys.argv) >= 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    else:
        print("The first argument must be the filename")
        print("The second argument indicates if the duplicate words must be deleted")
        sys.exit(1)

    print(f"The words of the file {filename} will be read")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"The file {filename} doesn't exist")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(items=word_list, ascending=sortOrder))
