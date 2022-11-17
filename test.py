class Driver:
    def __init__(self, id, is_available=True):
        self.id = id
        self.is_available = is_available


class Rider:
    def __init__(self, location):
        self.location = location

    def change_driver_availablity(self):
        driver2.is_available = False


driver1 = Driver(1, is_available=False)
driver2 = Driver(2)
print(driver2.is_available)

rider1 = Rider("new york")
rider1.change_driver_availablity()
print(f"Driver 2 availablity changed to {driver2.is_available}")
