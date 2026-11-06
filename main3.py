#PROJECT-1
# Student-Performance-Tracker
class student:
    def __init__(self , name , marks , attendance):
        self.name = name
        self.marks = marks
        self.attendance = attendance

    def calculate_average(self):
        avg = sum(self.marks) / len(self.marks)
        return avg

class Tracker:
    def __init__(self):
        self.student = []

    def add_student(self , student_obj):
        self.student.append(student_obj)

    def analyze_all(self):
        for student in self.student:
            avg = student.calculate_average()
            if avg < 50 or student.attendance < 75:
                print(f"{student.name} need improvment")
            else:
                print(f"{student.name} is doing great")

my_tracker = Tracker()

s1 = student("krishna" , [80 , 85 , 90] , 85)
my_tracker.add_student(s1)

s2 = student("Abhishek" , [40 , 45 , 50] , 60)
my_tracker.add_student(s2)

s3 = student("Aditya" , [35 , 40 , 42] , 80)
my_tracker.add_student(s3)

print("--------  EduTrack OOP Analysis Results --------")
my_tracker.analyze_all()


#PROJECT-2
# BANKING SYSTEM
class BankAccount:
    def __init__(self , account_holder , balance , pin):
        self.account_holder = account_holder
        self.__balance = balance
        self.__pin = pin

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposit successfully")
        else:
            print("Error: Amount must be greater than 0")

    def withdraw(self, amount , entered_pin):
        if entered_pin == self.__pin and amount <=self.__balance:
            self.__balance -= amount
            print(f"{amount} withdraw successfully")
        else:
            print("Error: Invailed pin! Cannot fetch balance")

    def get_balance(self , entered_pin):
        if entered_pin == self.__pin:
            return self.__balance
        else:
            print("Error: Invailed pin! Cannot fetch balance")
            return None
             
        

my_account = BankAccount("krishna" , 1000 , "1234")

my_account.__balance = 500000

my_account.deposit(500)

print("Current balance:" , my_account.get_balance("1234"))
        
#PROJECT-3
# SCHOOL LIBRARY MANAGEMENT SYSTEM
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("The library is currently empty")
            return
        for book in self.books:
            if book.is_issued == True:
                status = "Not available"
            else:
                status = "available"
            
            print(f"Title:{book.title} | Author: {book.author} | Status: {status}")

    def issue_book(self, title):
        found = False
        for book in self.books:
            
            if book.title == title:
                found = True
                if book.is_issued == False:
                    book.is_issued = True
                    print(f"success: '{title}' has been issued successfully")
                else:
                    print(f"Error: '{title}' is already issued")
                break 
                
        
        if found == False:
            print(f"Error: '{title}' not found in the library")


my_library = Library()

b1 = Book("Python basic", "harry")
b2 = Book("Data structure", "Love Babber")

my_library.add_book(b1)
my_library.add_book(b2)

print("---------Initial Library status-----------")
my_library.display_books()

print("\n-------Issuing 'Python basic'---------")
my_library.issue_book("Python basic")

print("\n-----------Library Status after After Issuing--------")
my_library.display_books()

print("\n------Testing Error Cases--------")
my_library.issue_book("Python basic")
my_library.issue_book("java programming")


#PROJECT-4
# Virtual Garage & Vehicle System
class Vehicle:
    def __init__(self , brand , model , speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self):
        self.speed +=10

    def show_status(self):
        print(f"vehicle brand:{self.brand} | Model: {self.model}|Current speed {self.speed}")

class Car(Vehicle):
    def __init__(self, brand, model, speed, doors):
        super().__init__(brand, model, speed)
        self.doors = doors

    def accelerate(self):
        self.speed +=20

class Bike(Vehicle):
    def __init__(self, brand, model, speed , has_carrier):
        super().__init__(brand, model, speed)
        self.has_carrier = has_carrier

    def accelerate(self):
        self.speed +=15

class Garage:
    def __init__(self):
        self.vehicle = []

    def add_vehicle(self , vehicle_object):
        self.vehicle.append(vehicle_object)

    def show_all(self):
        for v in self.vehicle:
            v.show_status()

garage = Garage()
garage.add_vehicle(Car("BMW", "M5", 10, 4))
garage.add_vehicle(Bike("Yamaha", "R15", 5, False))

for v in garage.vehicle:
    v.accelerate()

garage.show_all()

# PROJECT-5
# Atm Machine Simulator
class ATM:
    def __init__(self):
        self.balance = 0
        self.pin = "1234"
        self.menu()

    def menu(self):
        while True:
            print("\n--------ATM machine simulator----------")
            print("choose options: 1.check balance | 2.Deposit | 3.Withdraw | 4.change pin | 5.Exit")
            choice = input("Choose option (1-5): ")
            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.change_pin()
            elif choice == "5":
                print("Exit! Thank you for using ATM")
                break
            else:
                print("Invalid option! please try again")

    def check_balance(self):
        userpin = input("Enter your pin: ")
        if userpin == self.pin:
            print(f"Current Balance: {self.balance}")
        else:
            print("Wrong Pin! Access Denied")

    def deposit(self):
        amount = int(input("How much money needs to be deposited: "))
        if amount > 0:
            self.balance += amount
            print(f"{amount} Deposit successfully! New balance: {self.balance}")
        else:
            print("Invalid Amount!")

    def withdraw(self):
        userpin = input("Enter your PIN: ")
        if userpin == self.pin:
            amount = int(input("How much money needs to be withdrawn: "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount} withdraw successfully! Sufficient Balance")
                print(f"Remaining Balance: {self.balance}")
            else:
                print("Insufficient balance!")
        else:
            print("Wrong PIN! Access Denied.")
        
    def change_pin(self):
        userpin = input("Enter your current pin: ")
        if userpin != self.pin:
            print("Wrong current pin! No pin change")
            return
        new_pin = input("Enter your new pin: ")
        self.pin = new_pin
        print("PIN changed successfully!")

if __name__ == "__main__":
    my_atm = ATM()


#PROJECT-6
#E-Commerce Shopping Cart System
class Product:
    def __init__(self , name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class ShoppingCart:
    def __init__(self):
        self.cart_items = {}

    def add_to_cart(self, product_obj, quantity): 
        if product_obj.stock >= quantity:
            product_obj.stock -= quantity
            if product_obj.name in self.cart_items:
                self.cart_items[product_obj.name] +=quantity
            else:
                self.cart_items[product_obj.name] = quantity
            print(f"{quantity} x '{product_obj.name}' added to cart successfully!")
        else:
             print(f"Sorry! '{product_obj.name}' is out of stock or insufficient stock available")

    def view_cart(self):
        if len(self.cart_items) == 0:
            print("Your cart is currently empty!")
        else:
            print("\n------your shopping cart-------")
            for item_name, qty in self.cart_items.items():
                print(f"{item_name} - Quantity:{qty}")

    def calculate_bill(self,product_list):
        total_price = 0
        print("\n--------Bill summary-------")
        for item_name, qty in self.cart_items.items():
            for product in product_list:
                if product.name == item_name:
                    item_cost = qty * product.price
                    total_price += item_cost
                    print(f"{item_name}: {qty} x {product.price} = {item_cost}")
                    print("---------------------------------")
                    print(f"Total Amount Payable: {total_price}")

if __name__ == "__main__":
    laptop = Product("Laptop" , 50000,5)
    phone = Product("Mobile" , 15000,10)
    store_products = [laptop,phone]

    my_cart = ShoppingCart()
    my_cart.add_to_cart(laptop,2)
    my_cart.add_to_cart(laptop,1)
    my_cart.add_to_cart(phone,20)
    my_cart.view_cart()
    my_cart.calculate_bill(store_products )


#PROJECT-7
#SMART VENDING MACHINE
class Item:
    def __init__(self,name,price,code,stock=5):
        self.name = name
        self.price = price
        self.code = code
        self.stock = stock

    def display_item_details(self):
        print(f"Code: {self.code} | Item: {self.name} | price: {self.price} | Stock: {self.stock}")


class vendinMachine:
    def __init__(self):
        self.inventory = []
        self.total_cash = 0
        self.current_balance = 0

    def add_item_to_machine(self,item):
        self.inventory.append(item)

    def show_menu(self):
        print("\n-------VENDING MACHINE MENU--------")
        if not self.inventory:
            print("The machine is empty!")
            return
        for item in self.inventory:
            item.display_item_details()

    def insert_money(self,amount):
        if amount > 0:
            self.current_balance += amount
            print(f"successfully deposited: {amount} Current balance: {self.current_balance}")
        else:
            print("Please insert a vailed amount")

    def buy_product(self,code):
            target_item = None
            for item in self.inventory:
                if item.code.upper() == code.upper():
                    target_item = item
                    break

            if target_item is None:
                print("Invailed code! Please choose a vailed slot")
                return

            if target_item.stock <=0:
                print(f"Sorry, {target_item.name} is out of stock!")
                return

            if self.current_balance < target_item.price:
               print(f"Insufficient funds! {target_item.name} costs {target_item.name} Please deposit more money")
               return

            target_item.stock -=1
            self.total_cash += target_item.price

            change = self.current_balance - target_item.price
            print(f"Dispensing {target_item.name}...Enjoy your sanck!")

            if change > 0:
                print(f"Returning your change: {change}")
            self.current_balance = 0

if __name__ == "__main__":
    vm = vendinMachine()

    chips = Item("Lays chips" , 20 , "A1" , stock=2)
    soda = Item("coca cola" , 40 , "B1" , stock=5)

    vm.add_item_to_machine(chips)
    vm.add_item_to_machine(soda)

    vm.show_menu()

    print("\n------Attempting to buy without money-------")
    vm.buy_product("A1")

    print("\n------Inserting money-------")
    vm.insert_money(50)

    print("\n-------buying Item----------")
    vm.buy_product("A1")

    vm.show_menu()

#PROJECT-8
#Digital Movie Ticket Booking
class Movie:
    def __init__(self, title,genre,price):
        self.title = title
        self.genre = genre
        self.price = price

class Showtime:
    def __init__(self,movie,time,rows=3,cols=4):
        self.movie = movie
        self.time = time
        self.seating_grid = []
        for r in range(rows):
            row_list = []
            for c in range(cols):
                row_list.append("0")
            self.seating_grid.append(row_list)

    def display_seats(self):
        print(f"\n---------Seating Arrangement for {self.movie.title} ({self.time})--------")
        for r in range(len(self.seating_grid)):
            print(f"Row {r}:" , end="")
            for c in range(len(self.seating_grid[r])):
                print(f"[{self.seating_grid[r][c]}] " , end="")
            print()

    def reserve_seat(self,row_index,col_index):
        if row_index < 0 or row_index >= len(self.seating_grid) or col_index < 0 or col_index >= len(self.seating_grid[0]):
            print("Invailed seat coordinates!")
            return False
        
        if self.seating_grid[row_index][col_index] == "X":
            print("Sorry this seat is already booked!")
            return False
        else:
            self.seating_grid[row_index][col_index] = "X"
            return True

class BookingEngine:
    def __init__(self):
        self.shows = []

    def add_show(self,showtime_object):
        self.shows.append(showtime_object)

    def list_available_shows(self):
        if not self.shows:
            print("No active screening running today")
            return False
        
        for index in range(len(self.shows)):
            current_show = self.shows[index]
            print(f"[{index}] Title: {current_show.movie.title} | Time: {current_show.time} | Price: {current_show.movie.price}")
        return True

    def book_ticket(self,show_index,row,col):
        if show_index < 0 or show_index >= len(self.shows):
            print("Invailed movie selection index choice!")
            return False

        selected_show = self.shows[show_index]

        booking_success = selected_show.reserve_seat(row,col)
        if booking_success:
            print("\n===============================================")
            print("               TICKET CONFIRMED                  ")
            print("=================================================")
            print(f"Title: {selected_show.movie.title}| Time: {selected_show.time} | Row: {row}| seat: {col}|Price: {selected_show.movie.price}")
            print("======================================================")
            return True
        else:
            return False

if __name__ == "__main__":
    engine = BookingEngine()

    m1 = Movie("Inception" , "Sci-Fi" , 12)
    m2 = Movie("The Dark knight" , "Action" , 15)

    s1 = Showtime(m1 , "03:00 PM")
    s2 = Showtime(m2 , "07:30 PM")

    engine.add_show(s1)
    engine.add_show(s2)

    while True:
        print("\n-------- DIGITAL MOVIE TICKET BOOKING ---------")
        print("1.View Movie Schedules \n2.check seat layout \n3.Book Ticket  \n4.Exit")
        user_choice = input("Select an option (1-4):")
        if user_choice == "1":
            engine.list_available_shows()
        elif user_choice == "2":
            if engine.list_available_shows():
                try:
                    show_idx = int(input("Enter movie show index to view seating map:"))
                    if 0 <= show_idx < len(engine.shows):
                        engine.shows[show_idx].display_seats()
                    else:
                        print("Invailed show selection!")
                except ValueError:
                    print("Please enter numeric integers only")
               
        elif user_choice == "3":
            if engine.list_available_shows():
                try:
                    show_idx = int(input("Enter movie show index:"))
                    row_num = int(input("Enter Row number:"))
                    col_num = int(input("Enter seat number:"))
                    engine.book_ticket(show_idx , row_num , col_num)
                except ValueError:
                    print("Please enter vailed numeric integer choice only")

        elif user_choice == "4":
            print("Exiting system runtime program tracker...GoodBye!")
            break
        else:
            print("Invailed choice! Please select an option 1 and 4")


#PROJECT-9
#PYTHON CALCULATOR
print("-----------python calculator---------")
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
print("first number:" , num1)
print("second number:" , num2)
sum_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2
print("1.Addition" , num1 , "+" , num2, "=" ,sum_result)
print("2.subtrction", num1 , "-" , num2, "=" , sub_result)
print("3.multiplication" , num1, "*" , num2, "=", mul_result)
print("4.division" , num1, "/" , num2 , "=" , div_result)
print("end the program")

#PROJECT-10
 #Library Management System
class Library:
    def __init__(self):
        self.books_list = ["python" , "java" , "C++"]
        self.lent_books = {}

    def display_books(self):
        if len(self.books_list) ==0:
            print("there is no books in library")
        else:
           print("\n----Available books------")
           for books in self.books_list:
                print(books)
                print("----------------------\n")

    def borrow_book(self , book_name):
        if book_name in self.books_list:
            self.books_list.remove(book_name)
            print(f"successfully {book_name} has been issued to you")
        else:
            print(f"sorry, {book_name} is already issued to someone esle or does not exist")

    def return_book(self, book_name):
        self.books_list.append(book_name)
        print(f" {book_name} is successfully returned to library")

class Student:
    def request_book(self):
        book = input("Enter the name of the book you want to borrow: ")
        return book

    def return_book(self):
        book = input("Enter the name of the book you want to return:")
        return book

central_library = Library()
student_user = Student()

while True:
    print("\n1.Display book \n2. Request a book \n3. Return a book \n4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        central_library.display_books()
    elif choice == 2:
        requested_book = student_user.request_book()
        central_library.borrow_book(requested_book)
    elif choice == 3:
        returned_book = student_user.return_book()
        central_library.return_book(returned_book)
    elif choice == 4:
        print("Exiting Library System. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")


#PROJECT-11
#GoRide Core
class User:
    def __init__(self , user_id , name , phone , rating=5.0):
        self.user_id = user_id
        self.name = name
        self.phone = phone
        self.rating = rating

    def display_profile(self):
        print(f"Name: {self.name} | Phone: {self.phone} | Rating: {self.rating}/5.0")

class Rider(User):
    def __init__(self, user_id_, name, phone, rating=5.0 ,wallet_balance=0.0 , current_location=None):
        super().__init__(user_id_, name, phone, rating)
        self.wallet_balance = wallet_balance
        self.current_location = current_location

    def add_money(self , amount):
        if amount > 0:
            self.wallet_balance +=amount
            print(f"Amount {amount} added successfully. Current wallet Balance: {self.wallet_balance}")
        else:
            print("Error: Amount must be greater than 0!")

    def book_ride(self ,pickup_location , drop_location):
        print(f"\n[Booking Request] {self.name} wants a ride from '{pickup_location}' to '{drop_location}'")
        if self.wallet_balance < 50:
            print("Booking Failed Insufficient wallet balance. Please add money")
            return False
        else:
            self.current_location = pickup_location
            print("Booking Approved: Searching for nearby drivers...")
            return True

class Driver(User):
    def __init__(self, user_id_, name, phone , license_number, rating=5.0 ,is_available=True, current_vehicle=None):
        super().__init__(user_id_, name, phone, rating)
        self.license_number = license_number
        self.is_available = is_available
        self.current_vehicle = current_vehicle

    def accept_ride(self):
        if self.is_available:
            self.is_available = False
            print(f"Driver {self.name} has accepted the ride status: BUSY")
            return True
        else:
            print(f"Driver {self.name} is busy with another passenger")
            return False

    def complete_ride(self):
        self.is_available = True
        print(f"Driver {self.name} completed the ride. Status: AVAILABLE")

class Vehicle:
    def __init__(self , vehicle_number, model):
        self.vehicle_number = vehicle_number
        self.model = model

    def get_vehicle_details(self):
        print(f"Vehicle number: {self.vehicle_number}| Model: {self.model}")

    def calculate_fare(self ,distance):
        return 0

class Bike(Vehicle):
    def calculate_fare(self , distance):
        return distance * 5.0

class Sedan(Vehicle):
    def calculate_fare(self,distance):
        return distance * 12.0

class SUV(Vehicle):
    def calculate_fare(self,distance):
        return distance * 18.0

if __name__ == "__main__":
    print("==== TESTING RIDECRAFT PROJECT ====\n ")

    print("-------Creating Rider-------")
    rider1 = Rider("R101" , "Krishna" , "9876543210" , rating=4.8 , wallet_balance=30.0)
    rider1.display_profile()

    rider1.book_ride("Nagra" , "Jhansi station")

    rider1.add_money(200)
    rider1.book_ride("Nagra" , "Jhansi station")

    print("\n------- Creating Driver & Vehicle ----------")
    my_bike = Bike("UP-93-AB-1234" , "Splender plus")
    driver1 = Driver("D501" , "Amit kumar" , "9988776655" , rating=4.9 , license_number="DL-56789")

    driver1.current_vehicle = my_bike
    driver1.display_profile()
    my_bike.get_vehicle_details()

    distance_km = 10
    fare = driver1.current_vehicle.calculate_fare(distance_km)
    print(f"Calculated fore for {distance_km}km via bike: {fare}")

    print("\n------- Testing Driver Status Changes ---------")
    driver1.accept_ride()
    driver1.accept_ride()
    driver1.complete_ride()


#RPOJECT-12
#Hospital Patient & Doctor Management System
class Patient:
    def __init__(self, patient_id, name, age, gender, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease

    def display_patient_details(self):
        print(f"Patient ID: {self.patient_id} | Name: {self.name} | Age: {self.age} | Gender: {self.gender} | Disease: {self.disease}")


class Doctor:
    def __init__(self, doctor_id, name, specialization, availability=True):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.availability = availability

    def display_doctor_details(self):
        status_str = "Available" if self.availability else "On Leave"
        print(f"Doctor ID: {self.doctor_id} | Name: {self.name} | Specialization: {self.specialization} | Status: {status_str}")

    def update_availability(self, status):
        self.availability = status
        if self.availability:
            print(f"Dr. {self.name} is now available.")
        else:
            print(f"Dr. {self.name} is now on leave.")


class Appointment:
    def __init__(self, appointment_id, patient_id, doctor_id, appointment_date):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.status = "Scheduled"

    def display_appointment_details(self):
        print(f"Appointment ID: {self.appointment_id} | Patient ID: {self.patient_id} | Doctor ID: {self.doctor_id} | Date: {self.appointment_date} | Status: {self.status}")

    def cancel_appointment(self):
        self.status = "Cancelled"
        print(f"Appointment ID {self.appointment_id} has been cancelled successfully.")


class HospitalManagement:
    def __init__(self):
        self.patients_list = []
        self.doctors_list = []
        self.appointments_list = []

    def add_patient(self):
        print("\n--- Register New Patient ---")
        p_id = input("Enter Patient ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        gender = input("Enter Gender: ")
        disease = input("Enter Disease: ")
        
        new_patient = Patient(p_id, name, age, gender, disease)
        self.patients_list.append(new_patient)
        print("Patient successfully registered.")

    def add_doctor(self):
        print("\n--- Add New Doctor ---")
        d_id = input("Enter Doctor ID: ")
        name = input("Enter Name: ")
        spec = input("Enter Specialization: ")
        
        new_doctor = Doctor(d_id, name, spec)
        self.doctors_list.append(new_doctor)
        print("Doctor successfully added to the hospital system.")

    def book_appointment(self):
        print("\n--- Book an Appointment ---")
        p_id = input("Enter Patient ID: ")
        
        patient_found = False
        for p in self.patients_list:
            if p.patient_id == p_id:
                patient_found = True
                break
        
        if not patient_found:
            print("Error: Patient ID not registered. Please register the patient first.")
            return 

        d_id = input("Enter Doctor ID: ")
        
        doctor_to_book = None
        for d in self.doctors_list:
            if d.doctor_id == d_id:
                doctor_to_book = d
                break
        
        if doctor_to_book is None:
            print("Error: Doctor ID not found in the system.")
            return
            
        if not doctor_to_book.availability:
            print(f"Sorry: Dr. {doctor_to_book.name} is on leave today.")
            return

        app_id = input("Enter a unique Appointment ID: ")
        app_date = input("Enter Date (DD-MM-YYYY): ")
        
        new_app = Appointment(app_id, p_id, d_id, app_date)
        self.appointments_list.append(new_app)
        print("Success: Appointment successfully booked.")

    def cancel_appointment_by_id(self):
        print("\n--- Cancel an Appointment ---")
        app_id = input("Enter Appointment ID to cancel: ")
        
        for app in self.appointments_list:
            if app.appointment_id == app_id:
                app.cancel_appointment()
                return
        print("Error: Appointment ID not found.")

    def update_doctor_status(self):
        print("\n--- Update Doctor Availability ---")
        d_id = input("Enter Doctor ID: ")
        
        for d in self.doctors_list:
            if d.doctor_id == d_id:
                choice = input("Is the doctor available? (yes/no): ").lower()
                status = True if choice == "yes" else False
                d.update_availability(status)
                return
        print("Error: Doctor ID not found.")

    def view_all_details(self):
        print("\n================ SYSTEM DATABASE ================")
        print("\n--- Registered Doctors ---")
        if not self.doctors_list: 
            print("No doctors registered yet.")
        for doc in self.doctors_list: 
            doc.display_doctor_details()
        
        print("\n--- Registered Patients ---")
        if not self.patients_list: 
            print("No patients registered yet.")
        for pat in self.patients_list: 
            pat.display_patient_details()
        
        print("\n--- Booked Appointments ---")
        if not self.appointments_list: 
            print("No appointments scheduled yet.")
        for app in self.appointments_list: 
            app.display_appointment_details()
        print("=================================================")


if __name__ == "__main__":
    hospital = HospitalManagement()

    while True:
        print("\n--- HOSPITAL MANAGEMENT SYSTEM MENU ---")
        print("1. Add New Doctor")
        print("2. Register New Patient")
        print("3. Book an Appointment")
        print("4. Cancel an Appointment")
        print("5. Update Doctor Leave Status")
        print("6. View Hospital Database (All Details)")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            hospital.add_doctor()
        elif choice == "2":
            hospital.add_patient()
        elif choice == "3":
            hospital.book_appointment()
        elif choice == "4":
            hospital.cancel_appointment_by_id()
        elif choice == "5":
            hospital.update_doctor_status()
        elif choice == "6":
            hospital.view_all_details()
        elif choice == "7":
            print("\nThank you for using the Hospital Management System. Goodbye!")
            break
        else:
            print("Invalid Choice. Please enter a number between 1 and 7.")


#PROJECT-13
#Smart Chess Game
import io
import random
import tkinter as tk
from contextlib import redirect_stdout


def sign(number):
    if number > 0:
        return 1
    if number < 0:
        return -1
    return 0


class Piece:
    symbol = ""

    def __init__(self, colour, position, is_live=True):
        self.colour = colour
        self.position = position
        self.is_live = is_live

    def is_valid_move(self, start, end, board):
        return False

    def ends_on_own_piece(self, end, board):
        target = board.get_spot(end[0], end[1]).piece
        if target is not None and target.colour == self.colour:
            return True
        return False

    def is_path_clear(self, start, end, board):
        row_step = sign(end[0] - start[0])
        col_step = sign(end[1] - start[1])
        row = start[0] + row_step
        col = start[1] + col_step

        while (row, col) != end:
            if board.get_spot(row, col).piece is not None:
                return False
            row += row_step
            col += col_step
        return True


class Pawn(Piece):
    symbol = "\u265F"

    def is_valid_move(self, start, end, board):
        if self.colour == "White":
            direction = -1
            start_row = 6
        else:
            direction = 1
            start_row = 1

        row_diff = end[0] - start[0]
        col_diff = abs(end[1] - start[1])
        target = board.get_spot(end[0], end[1]).piece

        if col_diff == 0 and target is None:
            if row_diff == direction:
                return True
            if start[0] == start_row and row_diff == 2 * direction:
                middle_piece = board.get_spot(start[0] + direction, start[1]).piece
                return middle_piece is None
            return False

        if col_diff == 1 and row_diff == direction:
            return target is not None and target.colour != self.colour

        return False


class Rook(Piece):
    symbol = "\u265C"

    def is_valid_move(self, start, end, board):
        if self.ends_on_own_piece(end, board):
            return False
        same_row = start[0] == end[0]
        same_col = start[1] == end[1]
        if not (same_row or same_col):
            return False
        return self.is_path_clear(start, end, board)


class Knight(Piece):
    symbol = "\u265E"

    def is_valid_move(self, start, end, board):
        if self.ends_on_own_piece(end, board):
            return False
        row_diff = abs(end[0] - start[0])
        col_diff = abs(end[1] - start[1])
        return (row_diff, col_diff) in [(2, 1), (1, 2)]


class Bishop(Piece):
    symbol = "\u265D"

    def is_valid_move(self, start, end, board):
        if self.ends_on_own_piece(end, board):
            return False
        row_diff = abs(end[0] - start[0])
        col_diff = abs(end[1] - start[1])
        if row_diff != col_diff:
            return False
        return self.is_path_clear(start, end, board)


class Queen(Piece):
    symbol = "\u265B"

    def is_valid_move(self, start, end, board):
        if self.ends_on_own_piece(end, board):
            return False
        row_diff = abs(end[0] - start[0])
        col_diff = abs(end[1] - start[1])
        straight = row_diff == 0 or col_diff == 0
        diagonal = row_diff == col_diff
        if not (straight or diagonal):
            return False
        return self.is_path_clear(start, end, board)


class King(Piece):
    symbol = "\u265A"

    def is_valid_move(self, start, end, board):
        if self.ends_on_own_piece(end, board):
            return False
        row_diff = abs(end[0] - start[0])
        col_diff = abs(end[1] - start[1])
        return max(row_diff, col_diff) == 1


class Spot:
    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece


class Board:
    def __init__(self):
        self.grid = [[Spot(r, c) for c in range(8)] for r in range(8)]
        self.initialize_board()

    def initialize_board(self):
        for col in range(8):
            self.grid[1][col].piece = Pawn("Black", (1, col))
            self.grid[6][col].piece = Pawn("White", (6, col))

        order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for col, piece_class in enumerate(order):
            self.grid[0][col].piece = piece_class("Black", (0, col))
            self.grid[7][col].piece = piece_class("White", (7, col))

    def get_spot(self, row, col):
        return self.grid[row][col]


class Game:
    def __init__(self):
        self.board = Board()
        self.current_turn = "White"
        self.game_status = "ACTIVE"
        self.winner = None

    def player_move(self, start_row, start_col, end_row, end_col):
        start_spot = self.board.get_spot(start_row, start_col)
        end_spot = self.board.get_spot(end_row, end_col)
        piece = start_spot.piece

        if piece is None:
            print("There is no piece here!")
            return False

        if piece.colour != self.current_turn:
            print(f"It is {self.current_turn}'s turn!")
            return False

        if not piece.is_valid_move((start_row, start_col), (end_row, end_col), self.board):
            print("This move is not valid for this piece!")
            return False

        captured_piece = end_spot.piece
        if captured_piece is not None:
            captured_piece.is_live = False
            if isinstance(captured_piece, King):
                self.game_status = "FINISHED"
                self.winner = piece.colour

        end_spot.piece = piece
        piece.position = (end_row, end_col)
        start_spot.piece = None

        if self.current_turn == "White":
            self.current_turn = "Black"
        else:
            self.current_turn = "White"
        return True


class ComputerPlayer:
    def __init__(self, colour):
        self.colour = colour

    def choose_move(self, game):
        all_moves = []
        capture_moves = []

        for row in range(8):
            for col in range(8):
                piece = game.board.grid[row][col].piece
                if piece is None or piece.colour != self.colour:
                    continue

                for end_row in range(8):
                    for end_col in range(8):
                        start = (row, col)
                        end = (end_row, end_col)
                        if piece.is_valid_move(start, end, game.board):
                            all_moves.append((start, end))
                            if game.board.grid[end_row][end_col].piece is not None:
                                capture_moves.append((start, end))

        if capture_moves:
            return random.choice(capture_moves)
        if all_moves:
            return random.choice(all_moves)
        return None


SQUARE = 80
BAR = 50
BOARD_SIZE = SQUARE * 8

LIGHT_SQUARE = "#F0D9B5"
DARK_SQUARE = "#B58863"
SELECTED_SQUARE = "#F6F669"
LAST_MOVE_SQUARE = "#CDD26A"

ACTIVE_BAR = "#8BC34A"
INACTIVE_BAR = "#D0D0D0"


class ChessGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess - You vs Computer")
        self.game = Game()
        self.computer = ComputerPlayer("Black")
        self.selected = None
        self.last_move = None
        self.message = ""

        self.canvas = tk.Canvas(root, width=BOARD_SIZE, height=BOARD_SIZE + 2 * BAR,
                                highlightthickness=0)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)

        self.message_label = tk.Label(root, font=("Arial", 13), fg="red", pady=6)
        self.message_label.pack()

        self.draw()

    def draw(self):
        self.canvas.delete("all")
        self.draw_player_bars()
        self.draw_squares()
        self.draw_pieces()
        self.message_label.config(text=self.message)

    def draw_player_bars(self):
        bars = [
            ("Black", 0, 180),
            ("White", BAR + BOARD_SIZE, 0),
        ]
        for colour, top, angle in bars:
            is_active = self.game.game_status == "ACTIVE" and self.game.current_turn == colour
            is_winner = self.game.winner == colour

            if is_active or is_winner:
                bar_colour = ACTIVE_BAR
            else:
                bar_colour = INACTIVE_BAR

            if colour == "Black":
                text = "Black player (computer)"
            else:
                text = "White player (you)"
            if is_active:
                text += "  -  your turn"
            if is_winner:
                text += "  -  WINNER!"

            self.canvas.create_rectangle(0, top, BOARD_SIZE, top + BAR,
                                         fill=bar_colour, outline=bar_colour)
            self.canvas.create_text(BOARD_SIZE // 2, top + BAR // 2, text=text,
                                    angle=angle, font=("Arial", 16, "bold"))

    def draw_squares(self):
        for row in range(8):
            for col in range(8):
                x = col * SQUARE
                y = BAR + row * SQUARE

                if (row + col) % 2 == 0:
                    colour = LIGHT_SQUARE
                else:
                    colour = DARK_SQUARE

                if self.last_move and (row, col) in self.last_move:
                    colour = LAST_MOVE_SQUARE
                if self.selected == (row, col):
                    colour = SELECTED_SQUARE

                self.canvas.create_rectangle(x, y, x + SQUARE, y + SQUARE,
                                             fill=colour, outline=colour)

                if col == 0:
                    self.canvas.create_text(x + 8, y + 10, text=str(8 - row),
                                            fill="#555555", font=("Arial", 9))
                if row == 7:
                    self.canvas.create_text(x + SQUARE - 8, y + SQUARE - 10,
                                            text="abcdefgh"[col],
                                            fill="#555555", font=("Arial", 9))

    def draw_pieces(self):
        for row in range(8):
            for col in range(8):
                piece = self.game.board.grid[row][col].piece
                if piece is not None:
                    x = col * SQUARE + SQUARE // 2
                    y = BAR + row * SQUARE + SQUARE // 2
                    self.draw_piece(piece, x, y)

    def draw_piece(self, piece, x, y):
        if piece.colour == "White":
            fill = "white"
            angle = 0
        else:
            fill = "black"
            angle = 180

        font = ("Arial", 44)
        offsets = [(-2, 0), (2, 0), (0, -2), (0, 2), (-2, -2), (2, 2), (-2, 2), (2, -2)]
        for dx, dy in offsets:
            self.canvas.create_text(x + dx, y + dy, text=piece.symbol, font=font,
                                    fill="black", angle=angle)
        self.canvas.create_text(x, y, text=piece.symbol, font=font,
                                fill=fill, angle=angle)

    def on_click(self, event):
        if self.game.game_status != "ACTIVE":
            return
        if self.game.current_turn != "White":
            return

        row = (event.y - BAR) // SQUARE
        col = event.x // SQUARE
        if not (0 <= row < 8 and 0 <= col < 8):
            return

        clicked_piece = self.game.board.grid[row][col].piece
        turn = self.game.current_turn
        self.message = ""

        if self.selected is None:
            if clicked_piece is not None and clicked_piece.colour == turn:
                self.selected = (row, col)
            else:
                self.message = "Select one of your own pieces!"

        elif self.selected == (row, col):
            self.selected = None

        elif clicked_piece is not None and clicked_piece.colour == turn:
            self.selected = (row, col)

        else:
            start_row, start_col = self.selected
            output = io.StringIO()
            with redirect_stdout(output):
                moved = self.game.player_move(start_row, start_col, row, col)

            if moved:
                self.last_move = ((start_row, start_col), (row, col))
                if self.game.winner is not None:
                    self.message = f"{self.game.winner} wins! The King was captured."
                else:
                    self.root.after(700, self.computer_move)
            else:
                self.message = output.getvalue().strip()
            self.selected = None

        self.draw()

    def computer_move(self):
        if self.game.game_status != "ACTIVE":
            return

        move = self.computer.choose_move(self.game)
        if move is None:
            self.message = "Computer has no moves left."
            self.draw()
            return

        start, end = move
        self.game.player_move(start[0], start[1], end[0], end[1])
        self.last_move = (start, end)

        if self.game.winner is not None:
            self.message = f"{self.game.winner} wins! The King was captured."
        self.draw()


if __name__ == "__main__":
    root = tk.Tk()
    ChessGUI(root)
    root.mainloop()

#PROJECT-14
#Online Examination System
import time

class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    def login(self, input_email, input_password):
        if self.email == input_email and self.password == input_password:
            print(f"\n Welcome back, {self.name}! Login successfully")
            return True
        return False

class Student(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)
        self.my_results = []

    def view_available_exam(self, exam_list):
        print("\n---------------------AVAILABLE EXAMS-----------------------")
        if not exam_list:
            print("No exam are currently available")
            return 
        for idx, exam in enumerate(exam_list, 1):
            print(f"{idx}. [ID: {exam.exam_id}] {exam.title} ({exam.duration} Mins)")
            print("------------------------------------------------------------------")

    def view_past_results(self):
        print("\n-------------------YOUR REPORT CARD----------------------------")
        if not self.my_results:
            print("You have not taken any exams yet.")
            return
        for res in self.my_results:
            print(f"Exam: {res['exam_title']} | Score: {res['score']} | Status: {res['status']}")
            print("-----------------------------------------------------------------")

class Teacher(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)

    def create_exam(self, exam_id, title, duration):
        print(f"\n[System] Exam '{title}' successfully created by prof. {self.name}")
        return Exam(exam_id, title, duration)

class Question:
    def __init__(self, question_id, question_text, option_list, correct_option=1):
        self.question_id = question_id
        self.question_text = question_text
        self.option_list = option_list
        self.correct_option = correct_option

    def display_question(self):
        print(f"\nQ. {self.question_text}")
        for i, option in enumerate(self.option_list, 1):
            print(f"{i}) {option}")

    def check_answer(self, student_answer):
        return str(student_answer).strip() == str(self.correct_option).strip()

class Exam:
    def __init__(self, exam_id, title, duration):
        self.exam_id = exam_id
        self.title = title
        self.duration = duration
        self.questions_list = []

    def add_question(self, question_object):
        self.questions_list.append(question_object)

    def start_exam(self):
        print(f"\n================= EXAM START: {self.title.upper()}=====================")
        print(f"Duration: {self.duration} Minute | Total Question: {len(self.questions_list)}")
        print("Best of luck! The test is starting now...\n")
        time.sleep(1)

        score = 0
        if not self.questions_list:
             print("There are no questions in this exam!")
             return 0
        for idx, q in enumerate(self.questions_list, 1):
             print(f"\n---------- Question {idx} ---------")
             q.display_question()

             ans = input("Select the correct option (1-4): ")
             if q.check_answer(ans):
                 print("correct Answer!")
                 score += 1
             else:
                 print(f"Wrong! the option was {q.correct_option}.")

        print("\n======================== EXAM SUBMITTED====================")
        return score

class OnlineExamSystem:
    def __init__(self):
        self.users = {}
        self.exams = []

    def setup_dummy_data(self):
        teacher = Teacher(101, "Vishal sharma", "teacher@gmail.com", "pass123")
        student = Student(201, "Krishna", "student@gmail.com", "pass456")

        self.users[teacher.email] = teacher
        self.users[student.email] = student

        exam = teacher.create_exam("EX-501", "Python OOPs Quiz", 10)
        q1 = Question(1, "Which OOPs concept is used to hide internal data details?", 
                      ["Inheritance", "Encapsulation", "Polymorphism", "Abstraction"], 2)
        q2 = Question(2, "Which keyword is used to call a parent class constructor in Python?", 
                      ["super()", "this()", "parent()", "init()"], 1)

        exam.add_question(q1)
        exam.add_question(q2)
        self.exams.append(exam)

    def run(self):
        self.setup_dummy_data()

        while True:
            print("\n======================================================")
            print("         ONLINE EXAMINATION SYSTEM MENU             ")
            print("====================================================")
            print("1.Login")
            print("2.Exit")
            choice = input("Select an option (1-2): ")

            if choice == "2":
                print("Exiting system. Goodbye!")
                break

            if choice == "1":
                email = input("Enter Email: ")
                password = input("Enter Password: ")

                if email in self.users and self.users[email].login(email, password):
                    user = self.users[email]

                    if isinstance(user, Student):
                        while True:
                            print(f"\n------- STUDENT PANEL ({user.name})---------")
                            print("1.View Available Exams")
                            print("2.Attempts an Exams")
                            print("3.View past Results")
                            print("4.Logout")
                            s_choice = input("Select an option: ")

                            if s_choice == "1":
                                user.view_available_exam(self.exams)
                            elif s_choice == "2":
                                user.view_available_exam(self.exams)
                                if self.exams:
                                    try:
                                        ex_idx = int(input("Enter the exam number you wish to take: "))
                                        if 1 <= ex_idx <= len(self.exams):
                                            selected_exam = self.exams[ex_idx - 1]
                                            final_score = selected_exam.start_exam()
                                            status = "Pass" if final_score >= (len(selected_exam.questions_list)/2) else "Fail"
                                            user.my_results.append({
                                                "exam_title": selected_exam.title,
                                                "score": f"{final_score} / {len(selected_exam.questions_list)}",
                                                "status": status
                                            })
                                        else:
                                            print("Invalid exam choice number.")
                                    except ValueError:
                                        print("Please enter a valid numeric number")
                            elif s_choice == "3":
                                user.view_past_results()
                            elif s_choice == "4":
                                print("Logged out successfully")
                                break

                    elif isinstance(user, Teacher):
                        while True:
                            print(f"\n------------- TEACHER PANEL (prof. {user.name})------------")
                            print("1.Create New Exam")
                            print("2.Logout")
                            t_choice = input("Select an option: ")

                            if t_choice == "1":
                                e_id = input("Enter Exam ID: ")
                                title = input("Enter Exam Title: ")
                                try:
                                    dur = int(input("Enter Duration (in Minutes): "))
                                except ValueError:
                                    print("Invalid input. Defaulting to 10 minutes.")
                                    dur = 10
                                    
                                new_exam = user.create_exam(e_id, title, dur)
                                
                                while True:
                                    add_q = input("Do you want to add a question? (y/n): ")
                                    if add_q.lower() != 'y':
                                        break
                                    q_text = input("Enter question: ")
                                    opts = [input("Opt 1: "), input("Opt 2: "), input("Opt 3: "), input("Opt 4: ")]
                                    correct = input("Correct option (1-4): ")
                                    
                                    new_q = Question(len(new_exam.questions_list) + 1, q_text, opts, correct)
                                    new_exam.add_question(new_q)
                                    
                                self.exams.append(new_exam)
                                print("[System] Exam published successfully!")
                                
                            elif t_choice == "2":
                                print("Logged out successfully")
                                break
                else:
                    print("Invalid email or password.")

if __name__ == "__main__":
    system = OnlineExamSystem()
    system.run()

#PROJECT-15
#WealthMatrix
class User:
    def __init__(self, username, initial_balance):
        self.username = username
        self.balance = float(initial_balance)
        self.expenses = []

    def add_income(self, amount):
        amount = float(amount)
        if amount > 0:
            self.balance = self.balance + amount
            print("Amount Successfully added!")
        else:
            print("Invalid amount! Amount must be greater than 0")

    def get_balance(self):
        print(f"Current Balance: {self.balance}")

    def view_profile(self):
        print(f"username: {self.username} | Current balance: {self.balance}")


class Expense:
    def __init__(self, amount, category, description, date):
        self.amount = float(amount)
        self.category = category
        self.description = description
        self.date = date

    def get_expense_details(self):
        print(f"Date: {self.date} | Category: {self.category} | Description: {self.description} | Amount: {self.amount}")


class BudgetManager:
    def __init__(self, user_object):
        self.user = user_object 

    def add_expense(self, amount, category, description, date):
        amount = float(amount)
        if amount > self.user.balance:
            print(f"Insufficient balance! Your current balance is {self.user.balance}")
        else:
            self.user.balance = self.user.balance - amount
            new_expense = Expense(amount, category, description, date)
            self.user.expenses.append(new_expense)
            print("Expense added successfully")

    def view_all_expenses(self):
        print("\n------ ALL EXPENSES --------")
        if len(self.user.expenses) == 0:
            print("No expenses recorded yet")
        else:
            for exp in self.user.expenses:
                exp.get_expense_details()


print("----------- Welcome to Wealthmatrix --------------")
name = input("Enter your name:")
start_balance = input("Enter your initial balance:")

current_user = User(name, start_balance)
manager = BudgetManager(current_user)

while True:
    print("\n------ MENU -------")
    print("1. Add income")
    print("2. Add Expense")
    print("3. Check balance")
    print("4. View expense history")
    print("5. View profile")
    print("6. Exit app")

    choice = input("choose an option (1-6): ")

    if choice == "1":
        inc_amount = input("Enter income amount:")
        current_user.add_income(inc_amount)

    elif choice == "2":
        exp_amount = input("Enter expense amount:")
        cat = input("Enter category (food/travel etc.):")
        desc = input("Enter description:")
        dt = input("Enter date (DD-MM-YYYY): ")
        manager.add_expense(exp_amount, cat, desc, dt)

    elif choice == "3":
        current_user.get_balance()
        
    elif choice == "4":
        manager.view_all_expenses()
        
    elif choice == "5":
        current_user.view_profile()
        
    elif choice == "6":
        print("Thank you for using Wealthmatrix. Goodbye!")
        break
        
    else:
        print("Invalid choice! please select between 1 to 6")


#PROJECT-16
#Stock Market Trading & Portfolio Simulator
import random

class Stock:
    def __init__(self, ticker, company_name, current_price):
        self.ticker = ticker.upper()
        self.company_name = company_name
        self.current_price = float(current_price)
        self.price_history = [self.current_price]

    def update_price(self, percentage_change):
        change_amount = self.current_price * (percentage_change / 100)
        self.current_price += change_amount
        self.price_history.append(round(self.current_price, 2))
        self.current_price = round(self.current_price, 2)


class Portfolio:
    def __init__(self):
        self.shares = {}
        self.buy_prices = {}

    def add_stock(self, ticker, qty, price):
        ticker = ticker.upper()
        if ticker in self.shares:
            total_cost = (self.shares[ticker] * self.buy_prices[ticker]) + (qty * price)
            self.shares[ticker] += qty
            self.buy_prices[ticker] = round(total_cost / self.shares[ticker], 2)
        else:
            self.shares[ticker] = qty
            self.buy_prices[ticker] = round(price, 2)

    def remove_stock(self, ticker, qty):
        ticker = ticker.upper()
        if ticker in self.shares and self.shares[ticker] >= qty:
            self.shares[ticker] -= qty
            if self.shares[ticker] == 0:
                del self.shares[ticker]
                del self.buy_prices[ticker]
            return True
        return False

    def calculate_value(self, market_stocks):
        total_value = 0.0
        for ticker, qty in self.shares.items():
            if ticker in market_stocks:
                total_value += qty * market_stocks[ticker].current_price
        return round(total_value, 2)


class User:
    def __init__(self, name, initial_balance):
        self.name = name
        self.initial_balance = float(initial_balance)
        self.portfolio = Portfolio()

    def buy(self, stock_obj, qty):
        if qty <= 0:
            print("Quantity must be greater than zero.")
            return False
        
        required_money = stock_obj.current_price * qty
        if self.initial_balance >= required_money:
            self.initial_balance -= required_money
            self.portfolio.add_stock(stock_obj.ticker, qty, stock_obj.current_price)
            print(f"Successfully bought {qty} shares of {stock_obj.ticker}.")
            return True
        else:
            print(f"Error: Insufficient funds. Required: ${round(required_money, 2)}, Available: ${round(self.initial_balance, 2)}")
            return False

    def sell(self, stock_obj, qty):
        ticker = stock_obj.ticker.upper()
        if ticker not in self.portfolio.shares or self.portfolio.shares[ticker] < qty:
            print(f"Error: You do not own enough shares of {ticker}.")
            return False
        if qty <= 0:
            print("Quantity must be greater than zero.")
            return False
        
        if self.portfolio.remove_stock(ticker, qty):
            earnings = stock_obj.current_price * qty
            self.initial_balance += earnings
            print(f"Successfully sold {qty} shares of {ticker} for ${round(earnings, 2)}.")
            return True
        return False

    def display_profile(self, market_stocks):
        print("\n==========================================")
        print(f"TRADER PROFILE: {self.name}")
        print(f"Wallet Balance: ${round(self.initial_balance, 2)}")
        portfolio_value = self.portfolio.calculate_value(market_stocks)
        print(f"Portfolio Value: ${portfolio_value}")
        print(f"Total Net Worth: ${round(self.initial_balance + portfolio_value, 2)}")
        print("---------------------------------------")
        print("Current Holdings:")
        if not self.portfolio.shares:
            print("  (No stocks in portfolio)")
        else:
            for ticker, qty in self.portfolio.shares.items():
                avg_p = self.portfolio.buy_prices[ticker]
                curr_p = market_stocks[ticker].current_price
                pnl = round((curr_p - avg_p) * qty, 2)
                pnl_str = f"+${pnl}" if pnl >= 0 else f"-${abs(pnl)}"
                print(f"  * {ticker}: {qty} Shares | Avg Price: ${avg_p} | Current Price: ${curr_p} | PnL: {pnl_str}")
        print("==========================================")


class MarketSimulator:
    def __init__(self):
        self.user = None
        self.all_stocks = {}

    def add_market_stock(self, stock_obj):
        self.all_stocks[stock_obj.ticker] = stock_obj

    def simulate_day(self):
        print("\nTrading Day End: Market Prices Fluctuate...")
        for stocks in self.all_stocks.values():
            percentage_change = random.uniform(-5.0, 5.0)
            stocks.update_price(percentage_change)
            print(f" * {stocks.ticker}: {round(percentage_change, 2)}% -> New Price: ${stocks.current_price}")

    def show_market(self):
        print("\nCURRENT MARKET PRICES")
        print("----------------------------------------------------")
        for stocks in self.all_stocks.values():
            print(f"Search: {stocks.ticker} ({stocks.company_name}) : ${stocks.current_price}")
        print("----------------------------------------------------")

    def start(self):
        print("--------------- Welcome to Stock Market Simulator -------------------")
        name = input("Enter your username: ")
        balance = float(input("Enter initial starting wallet balance: "))
        self.user = User(name, balance)

        self.add_market_stock(Stock("AAPL", "Apple Inc.", 150.0))
        self.add_market_stock(Stock("TSLA", "Tesla Motors", 250.0))
        self.add_market_stock(Stock("MSFT", "Microsoft Corp.", 320.0))
        self.add_market_stock(Stock("AMZN", "Amazon.com Inc.", 180.0))

        while True:
            print("\nMAIN MENU:")
            print("1. View Market Prices")
            print("2. Buy Stocks")
            print("3. Sell Stocks")
            print("4. View My Portfolio / Profile")
            print("5. End Day (Fluctuate Market)")
            print("6. Exit")

            choice = input("Select an option (1-6): ")
            if choice == "1":
                self.show_market()
            elif choice == "2":
                self.show_market()
                ticker = input("Enter Stock Ticker to Buy: ").upper()
                if ticker in self.all_stocks:
                    try:
                        qty = int(input(f"How many shares of {ticker}?: "))
                        self.user.buy(self.all_stocks[ticker], qty)
                    except ValueError:
                        print("Invalid quantity! Please enter a valid number.")
                else:
                    print("This stock ticker does not exist in the market!")
            elif choice == "3":
                if not self.user.portfolio.shares:
                    print("You do not own any stocks to sell!")
                    continue
                ticker = input("Enter Stock Ticker to Sell: ").upper()
                if ticker in self.all_stocks:
                    try:
                        qty = int(input(f"How many shares of {ticker} to sell?: "))
                        self.user.sell(self.all_stocks[ticker], qty)
                    except ValueError:
                        print("Invalid quantity!")
                else:
                    print("Invalid stock ticker!")
            elif choice == "4":
                self.user.display_profile(self.all_stocks)
            elif choice == "5":
                self.simulate_day()
            elif choice == "6":
                final_worth = self.user.initial_balance + self.user.portfolio.calculate_value(self.all_stocks)
                print(f"\nGoodbye {self.user.name}! Final Net Worth: ${round(final_worth, 2)}")
                break
            else:
                print("Invalid option, please select between 1-6.")


if __name__ == "__main__":
    sim = MarketSimulator()
    sim.start()
        