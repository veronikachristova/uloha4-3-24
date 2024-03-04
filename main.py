class Kalkulacka:
    def __init__(self):
        self.numbers = {15, 47, 122, 4, 5, 45}

    def sum(self):
        return sum(self.numbers)

    def mean(self):
        average = sum(self.numbers) / len(self.numbers)
        return average

    def max(self):
        return max(self.numbers)

    def min(self):
        return min(self.numbers)
