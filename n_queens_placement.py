def nqueens_all_sol(n):

    counter = 0

    def solution_found(sol):
        nonlocal counter
        counter += 1
        print(counter, sol)

    def nqueens_sol_helper(i, free_rows, free_pdiags, free_sdiags, sol):

        if i == n:
            solution_found(sol)
        else:
            for k in range(0, n):

                pdiag_index = i - k + n - 1
                sdiag_index = i + k
                if (free_rows[k]
                        and free_pdiags[pdiag_index]
                        and free_sdiags[sdiag_index]):

                    sol[i] = k
                    free_rows[k] = False
                    free_pdiags[pdiag_index] = False
                    free_sdiags[sdiag_index] = False

                    nqueens_sol_helper(i+1, free_rows, free_pdiags,
                                       free_sdiags, sol)

                    free_rows[k] = True
                    free_pdiags[pdiag_index] = True
                    free_sdiags[sdiag_index] = True

    free_rows = [True] * n
    free_pdiags = [True] * (2*n - 1)
    free_sdiags = [True] * (2*n - 1)
    sol = [None] * n
    nqueens_sol_helper(0, free_rows, free_pdiags, free_sdiags, sol)

nqueens_all_sol(4)