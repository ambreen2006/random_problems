import time


class Derangement:

    def __init__(self):
        pass

    def __call__(self, n):
        return self.find_derangement(n)

    def find_derangement(self, n):

        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return (n - 1) * (self.find_derangement(n - 1) + self.find_derangement(n - 2))


start = time.time()
derangement = Derangement()
for i in range(1, 30):
    result = derangement(i)
    print(f"Derangement of {i} is {result}")
end = time.time()
delta = end - start

print(f"Execution time: {delta}")
