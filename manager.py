from vector import Vector

class Manager:
    def __init__(self, filename):
        self.filename = filename
        self.vectors = []

    def read(self):
        with open(self.filename) as f:
            for line in f:
                v, scalar = line.strip().split('-')
                v = v.split(',')
                nums = [float(s) for s in v]
                v = Vector(*nums)
                scalar = float(scalar)
                self.vectors.append(v * scalar)