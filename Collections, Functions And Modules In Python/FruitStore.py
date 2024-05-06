class FoodManager:
    def __init__(self, fruit_list):
        self.fruit_stock = {}

    def add_fruit_stock(self, fruit_name, quantity):
       
        if fruit_name in self.fruit_stock:
            self.fruit_stock[fruit_name] += quantity
           
        else:
            self.fruit_stock[fruit_name] = quantity
        return self.fruit_stock     

    def view_fruit_stock(self):
        print("View Food Stock")
        for fruit, quantity in self.fruit_stock.items():
            print(f"{fruit}: {quantity}")

    def update_fruit_stock(self, fruit_name, new_quantity):
        if fruit_name in self.fruit_stock:
            self.fruit_stock[fruit_name] = new_quantity
            print(f"{fruit_name}: {new_quantity}")
        else:
            print("Fruit not found in stock")

    def get_fruit_stock(self):
        return self.fruit_stock.copy()


def main():
    stock = FoodManager(["apple", "mango", "watermelon"])
    stock.add_fruit_stock("apple", 50)
    stock.add_fruit_stock("mango", 50)
    stock.add_fruit_stock("watermelon", 50)

    while True:
        print("\nFruit Store")
        print("1. Manager")
        print("2. Customer")
        print("3. Exit")

        admin = int(input("Select your role: "))

        if admin == 1:
            print("\nFruit Market Manager")
            print("1. Add Fruit Stock")
            print("2. View Fruit Stock")
            print("3. Update Fruit Stock")

            manager_choice = int(input("Select your choice: "))

            if manager_choice == 1:
                fruit_name = input("Enter fruit name: ")
                quantity = int(input("Enter quantity: "))
                stock.add_fruit_stock(fruit_name, quantity)
                print("Updated Fruit Stock:")
                for fruit, quantity in stock.update_fruit_stock.items():
                    print(f"{fruit}: {quantity}")
                

            elif manager_choice == 2:
                stock.view_fruit_stock()

            elif manager_choice == 3:
                fruit_name = input("Enter fruit name to update stock: ")
                new_quantity = int(input("Enter new quantity: "))
                stock.update_fruit_stock(fruit_name, new_quantity)

            else:
                print("Invalid Input")

        elif admin == 2:
            print("\nCustomer")
            print("Displaying the fruits:")
            stock.get_fruit_stock()

            if stock:
                for fruit, quantity in stock.get_fruit_stock().items():
                    print(f"{fruit}: {quantity}")
            else:
                print("No fruits available.")

        elif admin == 3:
            print("Exiting Fruit Store. Goodbye!")
            break

        else:
            print("Invalid Input. Please enter a valid option.")


class FoodManager:
    def __init__(self, fruit_list):
        self.fruit_stock = {}

    def add_fruit_stock(self, fruit_name, quantity):
        if fruit_name in self.fruit_stock:
            self.fruit_stock[fruit_name] += quantity
        else:
            self.fruit_stock[fruit_name] = quantity

    def view_fruit_stock(self):
        print("View Food Stock")
        for fruit, quantity in self.fruit_stock.items():
            print(f"{fruit}: {quantity}")

    def update_fruit_stock(self, fruit_name, new_quantity):
        if fruit_name in self.fruit_stock:
            self.fruit_stock[fruit_name] = new_quantity
            print(f"{fruit_name}: {new_quantity}")
        else:
            print("Fruit not found in stock")

    def get_fruit_stock(self):
        return self.fruit_stock.copy()


def main():
    stock = FoodManager(["apple", "mango", "watermelon"])
    stock.add_fruit_stock("apple", 50)
    stock.add_fruit_stock("mango", 50)
    stock.add_fruit_stock("watermelon", 50)

    while True:
        print("\n Tops Fruit Store")
        print("1. Manager")
        print("2. Customer")
        print("3. Exit")

        admin = int(input("Select your role: "))

        if admin == 1:
            print("\n Fruit Market Manager")
            print("1. Add Fruit Stock")
            print("2. View Fruit Stock")
            print("3. Update Fruit Stock")

            manager_choice = int(input("Select your choice: "))

            if manager_choice == 1:
                fruit_name = input("Enter fruit name: ")
                quantity = int(input("Enter quantity: "))
                stock.add_fruit_stock(fruit_name, quantity)
                print("Updated Fruit Stock:")
                if stock:
                    for fruit, quantity in stock.get_fruit_stock().items():
                        print(f"{fruit}: {quantity}")
                    

            elif manager_choice == 2:
                stock.view_fruit_stock()

            elif manager_choice == 3:
                fruit_name = input("Enter fruit name to update stock: ")
                new_quantity = int(input("Enter new quantity: "))
                stock.update_fruit_stock(fruit_name, new_quantity)

            else:
                print("Invalid Input")

        elif admin == 2:
            print("\nCustomer")
            print("Displaying the fruits:")
            stock.get_fruit_stock()

            if stock:
                for fruit, quantity in stock.get_fruit_stock().items():
                    print(f"{fruit}: {quantity}")
            else:
                print("No fruits available.")

        elif admin == 3:
            print("Exiting Fruit Store. Goodbye!")
            break

        else:
            print("Invalid Input. Please enter a valid option.")



main()


            
            
            
          
