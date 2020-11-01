from functools import lru_cache


@lru_cache(maxsize=2)
def count_derangement(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (n - 1) * (count_derangement(n - 2) + count_derangement(n - 1))


print("Number of Elements {:>52}".format("Derangement Count"))
line = '-' * 71
print(line)

for i in range(1, 31):
    print(f"{i:5d} {count_derangement(i):65}")
