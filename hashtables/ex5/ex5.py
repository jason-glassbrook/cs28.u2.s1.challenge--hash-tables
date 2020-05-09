from collections import defaultdict as DefaultDict
import os


def finder(paths, queries):

    # map bases to paths
    bases_to_paths = DefaultDict(list)
    for p in paths:
        b = os.path.basename(p)
        bases_to_paths[b].append(p)

    # find query paths
    query_paths = []
    for q in queries:
        if q in bases_to_paths:
            query_paths.extend(bases_to_paths[q])

    return query_paths


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
