from collections import defaultdict as DefaultDict
import os


def finder(paths, queries):

    # map bases to paths, allowing duplicates
    base_to_paths_map = DefaultDict(list)
    for p in paths:
        b = os.path.basename(p)
        base_to_paths_map[b].append(p)

    # find paths matching queries
    matches = []
    for q in queries:
        if q in base_to_paths_map:
            matches.extend(base_to_paths_map[q])

    return matches


if __name__ == "__main__":
    files = [
        "/bin/foo",
        "/bin/bar",
        "/usr/bin/baz",
    ]
    queries = [
        "foo",
        "qux",
        "baz",
    ]
    print(finder(files, queries))
