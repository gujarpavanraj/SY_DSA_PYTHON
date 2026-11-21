
class ParkingHashTable:
    def __init__(self):
        self.table = []
        self.size = 0

    # Create Hash Table
    def createTable(self):
        self.size = int(input("Enter hash table size (max 20): "))

        if self.size <= 0 or self.size > 20:
            print("Invalid table size!")
            self.size = 0
            return

        self.table = [None] * self.size
        print("Hash table created successfully")

    # Hash Function
    def hashFunction(self, key):
        return key % self.size

    # Insert Without Replacement
    def insertWithoutReplacement(self, key):
        if self.size == 0:
            print("Create hash table first!")
            return

        index = self.hashFunction(key)

        # Check whether position is empty
        if self.table[index] is None:
            self.table[index] = key
            print("Parking slot allocated:", index)

        else:
            print("Collision at index", index)

            # Start linear probing
            next_index = (index + 1) % self.size
            count = 0

            # Search for empty position
            while self.table[next_index] is not None:
                next_index = (next_index + 1) % self.size
                count += 1

                if count >= self.size:
                    print("Hash table is full!")
                    return

            # Insert key
            self.table[next_index] = key
            print("Parking slot allocated:", next_index)

    # Insert With Replacement
    def insertWithReplacement(self, key):
        if self.size == 0:
            print("Create hash table first!")
            return

        index = self.hashFunction(key)

        # Check whether position is empty
        if self.table[index] is None:
            self.table[index] = key
            print("Parking slot allocated:", index)

        else:
            # Calculate home position of existing key
            home = self.hashFunction(self.table[index])

            # Check whether existing key belongs here
            if home != index:

                # Store existing key temporarily
                displacedKey = self.table[index]

                # Place new key at its home position
                self.table[index] = key

                # Find location for displaced key
                next_index = (index + 1) % self.size
                count = 0

                while self.table[next_index] is not None:
                    next_index = (next_index + 1) % self.size
                    count += 1

                    if count >= self.size:
                        print("Hash table is full!")
                        return

                # Place displaced key
                self.table[next_index] = displacedKey

                print("Parking slot allocated:", index)
                print("Displaced vehicle allocated:", next_index)

            else:
                # Existing key belongs to this position
                next_index = (index + 1) % self.size
                count = 0

                # Find next available slot
                while self.table[next_index] is not None:
                    next_index = (next_index + 1) % self.size
                    count += 1

                    if count >= self.size:
                        print("Hash table is full!")
                        return

                # Insert new key
                self.table[next_index] = key
                print("Parking slot allocated:", next_index)

    # Search Vehicle
    def search(self, key):
        if self.size == 0:
            print("Create hash table first!")
            return

        index = self.hashFunction(key)

        for i in range(self.size):
            current = (index + i) % self.size

            if self.table[current] == key:
                print("Vehicle found at parking slot:", current)
                return

        print("Vehicle not found!")

    # Display Hash Table
    def display(self):
        if self.size == 0:
            print("Create hash table first!")
            return

        print("\nHash Table")
        print("-------------------------")
        print("Slot\tVehicle Number")
        print("-------------------------")

        for i in range(self.size):
            if self.table[i] is None:
                print(i, "\tEMPTY")
            else:
                print(i, "\t", self.table[i])

        print("-------------------------")


# Main Program
parking = ParkingHashTable()

parking.createTable()

if parking.size > 0:
    while True:
        print("\nPARKING SLOT ALLOCATION SYSTEM")
        print("1. Insert Vehicle - Without Replacement")
        print("2. Insert Vehicle - With Replacement")
        print("3. Search Vehicle")
        print("4. Display Hash Table")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            vehicleNumber = int(input("Enter vehicle number: "))
            parking.insertWithoutReplacement(vehicleNumber)

        elif choice == 2:
            vehicleNumber = int(input("Enter vehicle number: "))
            parking.insertWithReplacement(vehicleNumber)

        elif choice == 3:
            vehicleNumber = int(input("Enter vehicle number: "))
            parking.search(vehicleNumber)

        elif choice == 4:
            parking.display()

        elif choice == 5:
            print("Program terminated.")
            break

        else:
            print("Invalid choice!")
