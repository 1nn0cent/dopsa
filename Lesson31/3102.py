class Acellularia:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Cellularia(Acellularia):
    def __init__(self, name):
        super().__init__(name)


class Prokaryota(Cellularia):
    def __init__(self, name):
        super().__init__(name)


class Eukaryota(Cellularia):
    def __init__(self, name):
        super().__init__(name)


class Unicellularia(Eukaryota):
    def __init__(self, name):
        super().__init__(name)


class Fungi(Eukaryota):
    def __init__(self, name):
        super().__init__(name)


class Plantae(Eukaryota):
    def __init__(self, name):
        super().__init__(name)


class Animalia(Eukaryota):
    def __init__(self, name):
        super().__init__(name)


