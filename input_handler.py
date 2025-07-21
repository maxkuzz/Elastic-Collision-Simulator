def user_input(msg):
    while True:
        try:
            res = float(input(msg))
            if res < 0:
                print(f"❌ Value must be greater than 0. Try again.")
                continue
            return res
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

def start_simulation():
    print("=== Welcome to Elastic Collision Simulator ===")
    print("Please enter sizes for each object (recommended < 200px)")
    s1 = user_input("Size for object 1 (px): ")
    s2 = user_input("Size for object 2 (px): ")

    print("Please enter initial velocities (recommended < 20 m/s)")
    v1 = user_input("Velocity for object 1 (m/s): ")
    v2 = user_input("Velocity for object 2 (m/s): ")

    print("Please enter masses for each object (> 0)")
    m1 = user_input("Mass for object 1 (kg): ")
    m2 = user_input("Mass for object 2 (kg): ")

    return s1, s2, v1, m1, v2, m2
