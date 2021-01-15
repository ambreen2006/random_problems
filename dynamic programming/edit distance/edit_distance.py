import numpy as np


def edit_distance(T: str, P: str) -> int:
    """Compute edit distance between the two strings using dynamic programming

    Arguments:
    T - text to convert
    P - pattern to convert to

    >>> edit_distance("POLYNOMIAL", "EXPONENTIAL")
    6
    >>> edit_distance("YOU SHOULD", "THOU SHALT")
    5
    """

    M = len(T)
    N = len(P)
    table = [[0]*M for _ in range(N)]

    # empty pattern, delete all characters from T
    text_deleted = np.arange(0, M+1)
    # empty text, insert all characters from P
    pattern_inserted = np.arange(1, N+1)

    # stack the column for inserted patter characters
    table = np.column_stack((pattern_inserted, table))
    # stack the row of characters deleted from text
    table = np.vstack((text_deleted, table))

    for i in range(1, N+1):
        for j in range(1, M+1):

            substitute_or_match = (1 if P[i-1] != T[j-1] else 0) + table[i-1][j-1]
            insertion = 1 + table[i][j-1]
            deletion = 1 + table[i-1][j]

            table[i][j] = min(substitute_or_match, insertion, deletion)

    return table[N][M]
