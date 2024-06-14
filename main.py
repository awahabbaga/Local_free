
class Local:
    def __init__(self, available, local_id, address):
        self._available = available
        self._id = local_id
        self._address = address

    def is_available(self):
        return self._available

    def set_available(self, available):
        self._available = available

    def get_id(self):
        return self._id

    def set_id(self, local_id):
        self._id = local_id

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address


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





if __name__ == "__main__":
    # Create an instance of the Local class
    local1 = Local(True, 1, "123 Main St")

    # Check if the local is available
    if local1.is_available():
        print(f"The local {local1.get_id()} at {local1.get_address()} is available.")
    else:
        print(f"The local {local1.get_id()} at {local1.get_address()} is not available.")

    # Set the local's availability to False
    local1.set_available(False)

    # Check again
    if local1.is_available():
        print(f"The local {local1.get_id()} at {local1.get_address()} is available.")
    else:
        print(f"The local {local1.get_id()} at {local1.get_address()} is not available.")