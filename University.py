class University:
    def __init__(self, name, pavilions=None):
        self.name = name
        self.pavilions = pavilions if pavilions is not None else []

    def add_pavilion(self, pavilion):
        self.pavilions.append(pavilion)

    def remove_pavilion(self, pavilion):
        self.pavilions.remove(pavilion)

    def get_pavilions(self):
        return self.pavilions