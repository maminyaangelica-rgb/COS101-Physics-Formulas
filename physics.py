# COS 101 Assignment
# Five Basic Physics Formulas

# 1. Speed = Distance / Time
def calculate_speed(distance, time):
    return distance / time


# 2. Acceleration = (Final Velocity - Initial Velocity) / Time
def calculate_acceleration(final_velocity, initial_velocity, time):
    return (final_velocity - initial_velocity) / time


# 3. Force = Mass x Acceleration
def calculate_force(mass, acceleration):
    return mass * acceleration


# 4. Kinetic Energy = 1/2 x Mass x Velocity squared
def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2


# 5. Weight = Mass x Acceleration due to Gravity
def calculate_weight(mass, gravity=9.8):
    return mass * gravity


# Example calculations
print("Speed:", calculate_speed(100, 20), "m/s")
print("Acceleration:", calculate_acceleration(30, 10, 5), "m/s^2")
print("Force:", calculate_force(10, 5), "N")
print("Kinetic Energy:", calculate_kinetic_energy(2, 4), "J")
print("Weight:", calculate_weight(10), "N")
