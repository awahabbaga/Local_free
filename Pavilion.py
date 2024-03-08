class Pavilion:
    def __init__(self, name, pavilion_id, address, locals=None):
        self.name = name
        self.id = pavilion_id
        self.address = address
        self.locals = locals if locals is not None else []

    def add_local(self, local):
        self.locals.append(local)

    def remove_local(self, local):
        self.locals.remove(local)

    def get_locals(self):
        return self.locals