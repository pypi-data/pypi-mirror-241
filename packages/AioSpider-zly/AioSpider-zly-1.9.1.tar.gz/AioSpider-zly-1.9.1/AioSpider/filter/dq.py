class DqueueFilter:

    def __init__(self, capacity, max_capacity=float('inf')):

        self.capacity = capacity
        self.max_capacity = max_capacity
        self._bloom = None
        self.y = 0
        self.count = 0

    @property
    def bloom(self):

        if self._bloom is None:
            self._bloom = [set()]

        if self.count // self.capacity != self.y:
            if self.count >= self.max_capacity:
                raise ValueError(
                    f"从数据库中加载到的数据数量已经超过最大限制，data_count：{self.count}, "
                    f"max_capacity：{self.max_capacity}"
                )
            self._bloom.append(set())
            self.y += 1

        return self._bloom[self.y]

    def add(self, item):
        self.bloom.add(item)
        self.count += 1

    def add_many(self, items):
        for item in items:
            self.add(item)

    def __contains__(self, item):
        return any(item in st for st in self._bloom) if self._bloom is not None else False

    def __len__(self):
        return self.count