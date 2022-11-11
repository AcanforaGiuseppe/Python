class SparseArray(dict):
    def __init__(self, values):
        self.lenght = len(values)
        for idx, value in enumerate(values):
            if value != 0:
                self[idx] = value

    def __len__(self):
        return self.lenght

    def __delitem__(self, index):
        if index < self.lenght:
            if index in self:
                super().__delitem__(index)
            for i in range(index + 1, list(self)[-1] + 1):
                if i in self:
                    self[i - 1] = self.pop(i)
            self.lenght -= 1
        else:
            raise IndexError()

    def __getitem__(self, index):
        if index < self.lenght:
            if index in self:
                return super().__getitem__(index)
            else:
                return 0
        else:
            raise IndexError()

    def append(self, value):
        if value != 0:
            self[self.lenght] = value
        self.lenght += 1

    def __str__(self):
        return str([self[i] for i in range(0, len(self))])
