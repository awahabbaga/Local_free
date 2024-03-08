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
