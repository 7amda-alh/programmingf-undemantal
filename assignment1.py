from enum import Enum
#Enum class to represent room availability status
class Availability_Status(Enum):
    AVAILABLE = "Available"
    BOOKED = "Booked"
#class representing a customer in the hotel system
class Customer:
    def __init__(self, customer_ID, first_Name, last_Name, email, phone_Number):
        #initializing the customer attributes
        self.__customer_ID = customer_ID
        self.__first_Name = first_Name
        self.__last_Name = last_Name
        self.__email = email
        self.__phone_Number = phone_Number

    #getter and setter methods for each attributes for customer:
    def set_customer_ID(self, customer_ID):
        self.__customer_ID = customer_ID
    def get_customer_ID(self):
        return self.__customer_ID

    def set_first_Name(self, first_Name):
        self.__first_Name = first_Name
    def get_first_Name(self):
        return self.__first_Name

    def set_last_Name(self, last_Name):
        self.__last_Name = last_Name
    def get_last_Name(self):
        return self.__last_Name

    def set_email(self, email):
        self.__email = email
    def get_email(self):
        return self.__email

    def set_password(self, password):
        self.__password = password
    def get_password(self):
        return self.__password
    #function to make a reservation
    def make_Reservation(self, date, room_type):
        print(f"Reservation made for room type {room_type} on {date}.")
    #function to view reservation details
    def view_Reservation(self):
        print("Reservation details for the customer:")
    #function to view charges related to a customer's booking
    def view_Charges(self):
        print("Display charges: ")
    #function for customer to login
    def login(self, email, password):
        print(f"Logged in with {email}.")
#class representing a hotel room
class Room:
    def __init__(self, room_Number, room_Type, price, availability_Status, services):
        # initializing room attributes
        self.__room_Number = room_Number
        self.__room_Type = room_Type
        self.__price = price
        self.__availability_Status = availability_Status
        self.__services= services

    # getter and setter methods for each attributes for room:
    def set_room_Number(self, room_Number):
        self.__room_Number = room_Number
    def get_room_Number(self):
        return self.__room_Number

    def set_room_Type(self, room_Type):
        self.__room_Type = room_Type
    def get_room_Type(self):
        return self.__room_Type

    def set_price(self, price):
        self.__price = price
    def get_price(self):
        return self.__price

    def set_availability_Status(self, availability_Status):
        self.__availability_Status = availability_Status
    def get_availability_Status(self):
        return self.__availability_Status

    def set_services(self, services):
        self.__services = services
    def get_services(self):
        return self.__services

    #function to check room availability for a specific date
    def check_Availability(self, date):
        print(f"Room availability for {date}: {self.availability_Status}")
    #function to book a room
    def book_Room(self, date):
        print(f"Room booked for {date}")
    #function to view room details
    def view_Details(self):
        print(f"Room details: Number {self.room_Number}, Type: {self.room_Type}")
#class representing a reservation made by the customer
class Reservation:
    def __init__(self, reservation_ID, check_In_Date, check_Out_Date, total_Cost, number_Of_Night):
        # initializing reservation attributes
        self.__reservation_ID = reservation_ID
        self.__check_In_Date = check_In_Date
        self.__check_Out_Date = check_Out_Date
        self.__total_Cost = total_Cost
        self.__number_Of_Night = number_Of_Night

    # getter and setter methods for each attributes for reservation:
    def set_reservation_ID(self, reservation_ID):
        self.__reservation_ID = reservation_ID
    def get_reservation_ID(self):
        return self.__reservation_ID

    def set_check_In_Date(self, check_In_Date):
        self.__check_In_Date = check_In_Date
    def get_check_In_Date(self):
        return self.__check_In_Date

    def set_check_Out_Date(self, check_Out_Date):
        self.__check_Out_Date = check_Out_Date
    def get_check_Out_Date(self):
        return self.__check_Out_Date

    def set_total_Cost(self, total_Cost):
        self.__total_Cost = total_Cost
    def get_total_Cost(self):
        return self.__total_Cost

    def set_number_Of_Night(self, number_Of_Night):
        self.__number_Of_Night = number_Of_Night
    def get_number_Of_Night(self):
        return self.__number_Of_Night

    #function to confirm the reservation
    def confirm_Reservation(self):
        print("Reservation confirmed.")
    #function to cancel the reservation
    def cancel_Reservation(self):
        print("Reservation cancelled.")
    #function to update the reservation details
    def update_Reservation(self, date, room_type):
        print(f"Reservation updated to {room_type} on {date}.")
    #function to view all reservations
    def view_Reservations(self):
        print("Viewing all reservations.")

#class representing a payment made by the customer
class Payment:
    def __init__(self, payment_ID, amount, payment_Method, payment_Date, payment_Status):
        #initializing payment attributes
        self.__payment_ID = payment_ID
        self.__amount = amount
        self.__payment_Method = payment_Method
        self.__payment_Date = payment_Date
        self.__payment_Status = payment_Status

    #getter and setter methods for each attributes for payment:
    def set_payment_ID(self, payment_ID):
        self.__payment_ID = payment_ID
    def get_payment_ID(self):
        return self.__payment_ID

    def set_amount(self, amount):
        self.__amount = amount
    def get_amount(self):
        return self.__amount

    def set_payment_Method(self, payment_Method):
        self.__payment_Method = payment_Method
    def get_payment_Method(self):
        return self.__payment_Method

    def set_payment_Date(self, payment_Date):
        self.__payment_Date = payment_Date
    def get_payment_Date(self):
        return self.__payment_Date

    def set_payment_Status(self, payment_Status):
        self.__payment_Status = payment_Status
    def get_payment_Status(self):
        return self.__payment_Status 

    #function to make the payment
    def make_Payment(self, amount):
        print(f"Payment of {amount} made successfully.")
    #function to refund a payment
    def refund_Payment(self):
        print("Payment has been refunded.")
    #function to view payment details
    def view_Payment_Details(self):
        print(f"Payment ID: {self.__payment_ID}, Amount: {self.__amount}, Method: {self.__payment_Method}, Date: {self.__payment_Date}")

# Created objects for customer, hotel room, reservation, and payment.
customer1 = Customer("123-678", "Ahmed", "Alhosani", "Ahmed@gmail.com", "505-661-1110")
hotel_room = Room(6234, "1 King Bed", 1000, Availability_Status.AVAILABLE, "Non-smoking")
reservation = Reservation("12345698", "September 29, 2024", "October 3, 2024", 5000, 2)
payment = Payment(3490, 5000, "Mastercard","September 29, 2024", "complete")

#Displayed details
print(f"Customer Name: {customer1.get_first_Name()} {customer1.get_last_Name()}")
print(f"Customer ID: {customer1.get_customer_ID()}")
print(f"Reservation ID: {reservation.get_reservation_ID()}")
print(f"Room Details: {hotel_room.get_room_Type()}")
print(f"Check-in Date: {reservation.get_check_In_Date()}")
print(f"Check-out Date: {reservation.get_check_Out_Date()}")
print(f"Total Cost: ${payment.get_amount()}")
print(f"Number of Nights: {reservation.get_number_Of_Night()}")
print(f"Payment Status: {payment.get_payment_Status()}")
print(f"Room Number: {hotel_room.get_room_Number()}")
print(f"Room Availability: {hotel_room.get_availability_Status().value}")
print(f"Payment Method: {payment.get_payment_Method()}")
print(f"Payment Date: {payment.get_payment_Date()}")
