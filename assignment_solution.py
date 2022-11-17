# Import statement goes here
import time


# Driver class will have similar methods and properties
# ..Like Rider with extra functionality.

# This is a dummy riders list
riders_list = [
    {
        "rider_id": 1,
        "pickup_time": 5,
        "pickup_address": "47 W 13th St, New York, NY 10011, USA",
        "pickup_location": [40.820240, -73.935944],
        "drop_off_address": "44 W 4th St, New York, NY 10012, USA"
    },
    {
        "rider_id": 2,
        "pickup_time": 6,
        "pickup_address": "20 Cooper Square, New York, NY 10003, USA",
        "pickup_location": [40.727840, -73.991539],
        "drop_off_address": "33 Washington Square W, New York, NY 10011, USA\r"
    },
    {
        "rider_id": 3,
        "pickup_time": 8,
        "pickup_address": "1 E 2nd St, New York, NY 10003, USA",
        "pickup_location": [40.725239, -73.991508],
        "drop_off_address": "129 Washington streey e New York NY 10011 USA"
    },
    {
        "rider_id": 4,
        "pickup_time": 13,
        "pickup_address": "75 3rd Ave, New York, NY 10003, USA",
        "pickup_location": [41.929192, -73.981262],
        "drop_off_address": "124 Broadway  New York NY 10025 USA"
    },
    {
        "rider_id": 5,
        "pickup_time": 9,
        "pickup_address": "Metrotech Center, Brooklyn, NY 11201, USA",
        "pickup_location": [40.7313843, -73.9882642],
        "drop_off_address": "502 Delency Street New York NY 1025"
    },
    {
        "rider_id": 6,
        "pickup_time": 21,
        "pickup_address": "40 E 7th St, New York, NY 10003, USA",
        "pickup_location": [40.728062, -73.988819],
        "drop_off_address": "536 Clinton Street New York NY 1100"
    },
    {
        "rider_id": 7,
        "pickup_time": 5,
        "pickup_address": "838 Broadway, New York, NY 10003, USA",
        "pickup_location": [40.7336279, -73.9908577],
        "drop_off_address": "105 Housetone Street New York NY 1200"
    },
    {
        "rider_id": 8,
        "pickup_time": 12,
        "pickup_address": "69 W 9th St, New York, NY 10011, USA",
        "pickup_location": [40.7342159, -73.9988314],
        "drop_off_address": "201 lexinton Avinue New York NY 20000"
    },
    {
        "rider_id": 9,
        "pickup_time": 10,
        "pickup_address": "371 7th Ave, New York, NY 10001",
        "pickup_location": [40.748712, -73.9916585],
        "drop_off_address": "102 Time Square New York NY 2001"
    },
    {
        "rider_id": 10,
        "pickup_time": 13,
        "pickup_address": "400 Broome St, New York, NY 10013, USA",
        "pickup_location": [40.72082, -73.997398],
        "drop_off_address": "524 Ozone Park New York NY 20000."
    }
]


class Driver:
    def __init__(self, driver_current_location, is_available=True):
        self.driver_current_location = driver_current_location
        self.is_available = is_available
        self.is_available_at = []


# Rider class instantiated
class Rider:
    def __init__(self, pickup_time, pickup_location, pickup_address, dropOff_address):
        # pickup_location must be a list with only 2 elements first one is latitude and the second one is longitude
        self.pickup_time = pickup_time
        self.pickup_location = pickup_location
        self.pickup_address = pickup_address  # pickup_address
        self.dropOff_address = dropOff_address
        self.dropoff_location = self.dropoff_location_calc()
        self.estimated_ride_duration = self.ride_duration_calc()
        # ride duration calculator

        def ride_duration_calc(self):
            total_distance_in_km = self.pickup_address - \
                self.dropOff_address  # TODO: This is just an assumption
            # TODO: assume it takes 1 hour to travel 1 kilometre.
            return total_distance_in_km * 1

        def dropoff_location_calc(self):
            # dropoff_location calculator based on dropoff_address. It can be achived by another module.
            pass

# Rider class instances will have a prefered ride


if __name__ == "__main__":
    driver1 = Driver("New York", is_available=False)
    print(driver1.is_available)
