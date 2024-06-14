import pytesseract
from PIL import Image

class Local:
    def __init__(self, local_id, address):
        self._id = local_id
        self._address = address
        self._availability = []

    def add_availability(self, start_time, end_time):
        self._availability.append((start_time, end_time))

    def is_available(self, check_time):
        for (start, end) in self._availability:
            if start <= check_time < end:
                return False
        return True

    def get_id(self):
        return self._id

    def get_address(self):
        return self._address


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

    def get_available_locals(self, check_time):
        available_locals = [local for local in self.locals if local.is_available(check_time)]
        return available_locals


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

    def get_available_locals_in_pavilion(self, pavilion_id, check_time):
        for pavilion in self.pavilions:
            if pavilion.id == pavilion_id:
                return pavilion.get_available_locals(check_time)
        return []


def extract_schedule_from_image(image_path):
    """
    Extract text from an image using OCR and parse it to determine the schedule.
    """
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)  # No language specified
    return text


def parse_schedule(schedule_info):
    lines = schedule_info.split('\n')
    locals = {}
    
    for i in range(0, len(lines), 5):
        if i + 4 < len(lines):
            course = lines[i].strip()
            type_ = lines[i + 1].strip()
            local_id = lines[i + 2].strip()
            time_range = lines[i + 3].strip().split(' - ')
            
            if len(time_range) == 2:
                start_time, end_time = time_range
                
                if local_id not in locals:
                    locals[local_id] = Local(local_id, f"Address for {local_id}")
                
                locals[local_id].add_availability(start_time, end_time)
    
    return locals


if __name__ == "__main__":
    # Path to the uploaded image
    image_path = 'IMG_1801.PNG'

    # Extract schedule information from the image
    schedule_info = extract_schedule_from_image(image_path)
    print(f"Extracted Schedule Information:\n{schedule_info}")

    # Parse the schedule information
    locals_dict = parse_schedule(schedule_info)

    # Create an instance of the Pavilion class and add locals to it
    pavilion1 = Pavilion("Pavilion A", 1, "789 Oak St")
    for local in locals_dict.values():
        pavilion1.add_local(local)

    # Create an instance of the University class and add pavilions to it
    university = University("University X")
    university.add_pavilion(pavilion1)

    # Check availability of a specific local at a specific time
    pavilion_id_to_check = 1
    time_to_check = "10h00"

    available_locals = university.get_available_locals_in_pavilion(pavilion_id_to_check, time_to_check)
    print(f"Available locals in Pavilion {pavilion_id_to_check} at {time_to_check}:")
    for local in available_locals:
        print(f"Local {local.get_id()} at {local.get_address()}")
