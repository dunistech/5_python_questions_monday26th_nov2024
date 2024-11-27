# lockers.py

def simulate_lockers():
    # Step 1: Initialize lockers (all closed)
    lockers = [False] * 100  # False means closed

    # Step 2: Simulate students toggling lockers
    for student in range(1, 101):  # Students S1 to S100
        for locker in range(student - 1, 100, student):  # Toggle every nth locker
            lockers[locker] = not lockers[locker]

    # Step 3: Determine open lockers
    open_lockers = [i + 1 for i, is_open in enumerate(lockers) if is_open]
    return open_lockers

def main():
    open_lockers = simulate_lockers()
    print("Open lockers after all students have toggled them:")
    print(open_lockers)

if __name__ == "__main__":
    main()