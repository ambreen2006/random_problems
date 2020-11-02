def generate_subsets(i, sol, elements):
    if i == len(elements):
        print_subset_binary(sol, elements)
    else:
        for k in [0, 1]:
            sol[i] = k
            generate_subsets(i+1, sol, elements)


def generate_subsets_wrapper(elements):
    sol = [None] * (len(elements))
    generate_subsets(0, sol, elements)


def print_subset_binary(sol, elements):
    no_elements = True
    print('{', end='')
    for i in range(0, len(sol)):
        if sol[i] == 1:
            if no_elements:
                print(elements[i], sep='', end='')
                no_elements = False
            else:
                print(', ', elements[i], sep='', end='')
    print('}')


generate_subsets_wrapper(['a', 'b', 'c'])