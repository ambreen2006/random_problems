class Derangement:

    def find_derangements_of_size(self, elements_size) -> [int]:

        def find_derangement_helper(elements, k):

            if k == len(elements):
                d_list.append(elements.copy())
                return

            for i in range(len(elements) - 1, k - 1, -1):
                if i == elements[k]:
                    continue

                elements[i], elements[k] = elements[k], elements[i]
                find_derangement_helper(elements, k + 1)
                elements[i], elements[k] = elements[k], elements[i]

        d_list = []
        elements = list(range(0, elements_size))
        find_derangement_helper(elements, 0)
        return d_list

    def __call__(self, original):

        d_list = self.find_derangements_of_size(len(original))
        deranged_perms = []
        for d in d_list:
            deranged_perms.append([original[x] for x in d])
        return deranged_perms


derangement = Derangement()
original = ['Snowball', 'Napoleon', 'Squealer', 'Old Major']
d_perms = derangement(original)

print("\n")
print(f'  {original}')
print('-' * 52)
for i, p in enumerate(d_perms):
    print(i + 1, p)

