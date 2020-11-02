def generate_subsets(i, sol, elements):

    if i == len(elements):
        print(sol)
    else:
        generate_subsets(i+1, sol, elements)
        generate_subsets(i+1, [elements[i]]+sol, elements)


generate_subsets(0, [], ['a', 'b', 'c'])