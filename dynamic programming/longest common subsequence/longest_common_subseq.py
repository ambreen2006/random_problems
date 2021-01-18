from enum import Enum, auto


class Direction(Enum):
    NONE = auto()
    LEFT = auto()
    UP = auto()


def lcs(a, b) -> str:
    """Returns the common subsequence in a and b as a string
    >>> lcs("FOSH", "FISH")
    Length of longest common subsequence is 3
    'FSH'
    >>> lcs("FOSH", "FORT")
    Length of longest common subsequence is 2
    'FO'
    """
    n = len(a)
    m = len(b)

    table = [[(0, Direction.NONE) for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):

            up, left = table[i - 1][j][0], table[i][j - 1][0]
            d, val = (Direction.UP, up) if up > left else (Direction.LEFT, left)
            if a[i-1] == b[j-1]:
                val += 1
            table[i][j] = (val, d)

    print(f'Length of longest common subsequence is {table[i][j][0]}')

    common = []
    d = table[i][j][1]
    while d != Direction.NONE:
        if a[i-1] == b[j-1]:
            common.append(a[i-1])
        if d == Direction.LEFT:
            j -= 1
        else:
            i -= 1
        d = table[i][j][1]

    common.reverse()
    return ''.join(common)


print(lcs("FOSH", "FISH"))
print(lcs("FOSH", "FORT"))