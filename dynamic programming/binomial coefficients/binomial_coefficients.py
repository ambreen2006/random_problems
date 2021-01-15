class BinomialCoefficients:
    _table = [[0]]

    @staticmethod
    def extend_table(extend_to):
        """Extend the table to the given row"""
        BinomialCoefficients.compute_pascal_triangle(len(BinomialCoefficients._table), extend_to)

    @staticmethod
    def compute_pascal_triangle(rows_begin, rows_end):
        """Compute Pascal Triangle
        Args
        ---
        rows_begin: start computing from rows
        rows_end: compute up to the rows
        """
        for i in range(rows_begin, rows_end+1):
            BinomialCoefficients._table.append([])
            for j in range(i+1):
                if j == 0 or j == i:
                    BinomialCoefficients._table[i].append(1)
                    continue

                right_above = 0
                if j < len(BinomialCoefficients._table[i-1]):
                    right_above = BinomialCoefficients._table[i-1][j]
                value_i_choose_k = BinomialCoefficients._table[i-1][j-1] + right_above
                BinomialCoefficients._table[i].append(value_i_choose_k)

    @staticmethod
    def print_table(table):
        """Pretty prints the pascal's triangle"""
        for i in range(len(table)):
            for j in range(len(table[0])):
                if table[i][j] == 0:
                    break
                print(f"{table[i][j]} ", end=" ")
            print("")

    @staticmethod
    def n_choose_k(n, k) -> int:
        """Returns the number of ways k can be chosen from n.
        If n exceeds the length of the cached, compute, otherwise return saved value
        """

        BC = BinomialCoefficients

        if k > n:
            return 0

        if n > len(BC._table):
            BC.extend_table(n)

        return BC._table[n][k]

    @staticmethod
    def precompute(n):
        """Computes or extends the pascal's triangle to n*n"""

        BC = BinomialCoefficients
        if len(BC._table) < n:
            BC.extend_table(n)


BinomialCoefficients.precompute(10)
print(BinomialCoefficients.n_choose_k(4, 3))
print(BinomialCoefficients.n_choose_k(7, 6))
