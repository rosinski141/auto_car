# autonomous vehicle function 1
vehicle_speed = 0
vehicle_direction = 'centre'

def set_speed(speed):
    if vehicle_speed != speed:
        vehicle_speed = speed

def set_direction(direction):
    if vehicle_direction != direction:
        vehicle_direction = direction

def stop_vehicle():
    vehicle_brake = False
    vehicle_accellerate = False
    vehicle_parking = True