from datetime import date #Importing the date class to handle date-related attributes

#represents an ebook in the catalog
class EBook:
    def __init__(self, title, author, publication_date, genre, price): # Initialize eBook with attributes
        # Private attribute
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price

#applyed getter and setter for each attribute and method
    def get_title(self):
        return self.__title
    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author
    def set_author(self, author):
        self.__author = author

    def get_publication_date(self):
        return self.__publication_date
    def set_publication_date(self, publication_date):
        self.__publication_date = publication_date

    def get_genre(self):
        return self.__genre
    def set_genre(self, genre):
        self.__genre = genre

    def get_price(self):
        return self.__price

#Setter for price with validation to avoid negative values
    def set_price(self, price):
        try:
            if price < 0: #Check if the price is negative
                raise ValueError("The price cannot be negative.") #Ensure price is not negative
            self.__price = price #Set price if valid
        except ValueError as ve:
            print(ve) #Prints an error message if the price is negative

#String representation of eBook for easy printing
    def __str__(self):
        return f"EBook: {self.__title} by {self.__author}, Genre: {self.__genre}, Price: ${self.__price}"


#Represents a shopping cart containing multiple e-books.
class ShoppingCart:
    def __init__(self): #Initialize ShoppingCart with empty list items
        self.__cart_items = [] #Aggregation: ShoppingCart can contain multiple EBooks
        self.__total_amount = 0.0 #to store the total amount of all items
        self.__ebook_count = 0 #to store the count of e-books in the cart

    # Getters and Setters for each attribute
    def get_cart_items(self):
        return self.__cart_items

    # Sets cart items only if all items are instances of EBook
    def set_cart_items(self, cart_items):
        try:
            if all(isinstance(item, EBook) for item in cart_items): #Validate all items are eBooks
                self.__cart_items = cart_items #Assign the validated cart items
                self.update_ebook_count()  #Update count and total when setting new items
                self.calculate_total()  #Recalculate total amount
            else:
                raise TypeError("All items must be instances of EBook.") #Raise error if non-eBook item is included
        except TypeError as te:
            print(te) #Output the error message

    def get_total_amount(self):
        return self.__total_amount
    def set_total_amount(self, total_amount):
        self.__total_amount = total_amount #Set the new total amount in the cart

    def get_ebook_count(self):
        return self.__ebook_count
    def set_ebook_count(self, ebook_count):
        self.__ebook_count = ebook_count

    #Adds an e-book to the cart (aggregation with EBook)
    def add_ebook(self, ebook: EBook):
        #Adds an EBook to the cart and updates count and total.
        if isinstance(ebook, EBook): #Checks if the item is an instance of EBook
            self.__cart_items.append(ebook) #Adds the eBook to the cart
            self.update_ebook_count() #Updates eBook count
            self.calculate_total() #Updates total amount
        else:
            print("Only EBook instances can be added to the cart.") #Prints error message for invalid item type

    #Removes an EBook from the cart and updates count and total
    def remove_ebook(self, ebook: EBook):
        try:
            self.__cart_items.remove(ebook) #Removes the eBook from the cart
            self.update_ebook_count() #Updates eBook count
            self.calculate_total() #Updates total amount
        except ValueError:
            print("EBook not found in cart.") #Prints error message if eBook is not in the cart

    #calculate the total amount of the cart
    def calculate_total(self):
        self.set_total_amount(sum(ebook.get_price() for ebook in self.__cart_items)) #Sum prices of all eBooks

    # update the count of e-books in the cart
    def update_ebook_count(self):
        self.set_ebook_count(len(self.__cart_items)) #Count total eBooks in cart and set it

    # String representation of ShoppingCart for easy printing
    def __str__(self):
        cart_contents = "\n".join(str(ebook) for ebook in self.__cart_items)
        return f"Shopping Cart:\n{cart_contents}\nTotal Amount: ${self.__total_amount}\nEBook Count: {self.__ebook_count}"


#represent a customer in the system
class Customer:
    def __init__(self, name, email, phone_number,address):# Initialize Customer with attributes
        #Private attribute for customer
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number
        self.__address = address
        self.__cart = ShoppingCart() # Aggregation Customer has a ShoppingCart but ShoppingCart exists independently

# apply getter and setter for each attribute and method
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email

    def get_phone_number(self):
        return self.__phone_number
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_address(self):
        return self.__address
    def set_address(self, address):
        self.__address = address

#Simulates browsing available e-books. In a full implementation, this would connect to a list of e-books.
    def browse_ebooks(self):
        print("Browsing available ebooks...") #Placeholder method for browsing eBooks

#Sets up account details for a new customer.
    def create_account(self, name, email, phone_number):
        self.set_name(name) #Set the customer's name
        self.set_email(email) #Set the customer's email
        self.set_phone_number(phone_number) #Set the customer's phone_number
        print(f"Account created for {self.get_name()} with email {self.get_email()} and phone number {self.get_phone_number()}")

#Completes a purchase by creating an Order based on the ShoppingCart contents.
    def make_purchase(self):
        if not self.__cart.get_cart_items(): #Check if the shopping cart is empty
            raise Exception("Shopping cart is empty. Add items to the cart before making a purchase.")
        #Here shows composition order with customer
        order = Order(self, self.__cart) #Composition: Order created with Customer
        self.__cart = ShoppingCart() #Reset the shopping cart after purchase
        print("Purchase completed.") #Confirm purchase
        return order

# Prints the invoice from the associated Order's Payment.
    def receive_invoice(self, order):
        if order is None:
            raise ValueError("No order provided.") #Raise error if no order is provided
        print("Receiving invoice...") #Print invoice message
        print(order.get_payment().generate_invoice()) #Call and print the generated invoice

# String representation of eBook for easy printing
    def __str__(self):
        return f"Customer: {self.__name}, Email: {self.__email}, Phone: {self.__phone_number}, Address: {self.__address}"

#represents an order with customer, ebooks, and order date
class Order:
    def __init__(self, order_id, ebooks, customer):#Initialize Order with customer and eBook list from ShoppingCart.
        # Private attribute for order
        self.__order_id = order_id
        self.__ebooks = ebooks  # Aggregation: Order can contain multiple EBooks
        self.__order_date = date.today() #Automatically set to today's date
        self.__total_amount = 0.0  # Initialize total_amount
        self.calculate_total_amount() # Calculates the total amount initially
        self.__customer = customer #  with Customer apply for discount calls
        self.__payment = Payment(self) # Composition with Payment
        self.apply_discounts()  # Apply discounts if any

    # Getter and setter methods
    def get_order_id(self):
        return self.__order_id

    def get_ebooks(self):
        return self.__ebooks
    def set_ebooks(self, ebooks):
        self.__ebooks = ebooks
        self.calculate_total_amount() # Recalculates total amount with new eBooks

    def get_order_date(self):
        return self.__order_date

    def get_total_amount(self):
        return self.__total_amount

    def get_customer(self):
        return self.__customer

    def get_payment(self):
        return self.__payment

# Method to calculate the total amount of the order
    def calculate_total_amount(self):#Sets the total amount by summing prices of all e-books in the order.
        self.__total_amount = sum(ebook.get_price() for ebook in self.__ebooks)

    # Applies discounts based on customer type and cart size
    def apply_discounts(self):
        self.calculate_total_amount() #Reset total amount before applying discounts
        if isinstance(self.__customer, LoyaltyMember): #Check if customer is a loyalty member
            self.__total_amount *= (1 - self.__customer.get_discount()) #Apply loyalty discount
        if len(self.__ebooks) >= 5: #Apply bulk discount if order contains 5 or more eBooks
            self.__total_amount *= 0.8 #20% discount for bulk purchase

#Method to simulate the delivery of e-books
    def deliver_ebooks(self):#Simulates instant delivery of all e-books in the order.
        for ebook in self.__ebooks: #Loop through all eBooks in the order
            print(f"Delivering e-book: {ebook}") #Print delivery message for each eBook

    #String representation of Order for easy printing
    def __str__(self):
        ebook_list = "\n".join(str(ebook) for ebook in self.__ebooks)
        return f"Order ID: {self.__order_id}\nCustomer: {self.__customer}\nEBooks:\n{ebook_list}\nTotal Amount: ${self.__total_amount}"

#Represents a payment for an order with VAT and final invoice.
class Payment:
    def __init__(self, order, vat_rate=0.08):# Initialize Payment with Order (Composition)
        self.__order = order # Composition: Payment is linked to a specific Order
        self.__vat_rate = vat_rate # VAT rate for the payment
        self.__final_amount = 0.0  # Initialize final amount
        self.apply_vat()  # Applies VAT to calculate the final amount
        self.__invoice = self.generate_invoice(order) # Stores the generated invoice details

# Getter and setter
    def get_vat_rate(self):
        return self.__vat_rate
    def set_vat_rate(self, vat_rate):
        if vat_rate < 0: #Validate VAT rate to be non-negative
            raise ValueError("VAT rate cannot be negative.") #Raise error for invalid VAT rate
        self.__vat_rate = vat_rate # Set the VAT rate

        self.apply_vat() # calculate a new final amount after changing VAT rate

    def get_final_amount(self):
        return self.__final_amount

    def get_invoice(self):
        return self.__invoice


#apply VAT to the final amount
    def apply_vat(self):
        #Applies the VAT to the current total amount to compute the final amount.
        subtotal = self.__order.get_total_amount() #Gets order subtotal
        self.__final_amount = subtotal * (1 + self.__vat_rate) #Calculate final amount with VAT

    # Method to generate an invoice
    def generate_invoice(self, order):
        #Generates an itemized invoice with e-book prices, applicable VAT, and the final total.
        ebook_list = "\n".join(f"- {ebook.get_title()} by {ebook.get_author()}: ${ebook.get_price()}" for ebook in order.get_ebooks()) #List eBooks in the order
        invoice = (
            f"Invoice for Order ID: {order.get_order_id()}\n"
            f"Customer: {order.get_customer().get_name()}\n\n"
            f"EBooks:\n{ebook_list}\n\n"
            f"Subtotal: ${order.get_total_amount()}\n"
            f"VAT ({self.__vat_rate * 100}%): ${order.get_total_amount() * self.__vat_rate}\n"
            f"Total (incl. VAT): ${self.__final_amount}\n"
        )
        return invoice #Return the formatted invoice as a string

    def __str__(self):
        return f"Payment - Final Amount (incl. VAT): ${self.__final_amount}"

#Represents the loyalty member, inheriting from Customer
class LoyaltyMember(Customer): #Inheritance from the Customer
    def __init__(self, name, email, phone_number, address, discount=0.10): #Initialize LoyaltyMember with attributes
        super().__init__(name, email, phone_number, address) #LoyaltyMember inherits Customer properties and used super(). methods constructor for Customer
        self.__discount = discount #Default discount of 10%

#Apply getter and setter for each attribute and method
    def get_discount(self):
        return self.__discount
    def set_discount(self, discount):
        try:
            if discount < 0 or discount > 1: #Validates discount range
                raise ValueError("Discount must be between 0 and 1.")
            self.__discount = discount #Set the discount if valid
        except ValueError as ve:
            print(ve) #Print error if discount is invalid

#Applies the loyalty member discount to the order.
    def apply_member_discount(self, order: Order):
        discount_amount = order.get_total_amount() * self.__discount #Calculate discount amount
        order.set_total_amount(order.get_total_amount() - discount_amount) #Apply discount to total

    # Method to apply bulk discount if 5 or more e-books are in the order
    def apply_bulk_discount(self, order: Order):
        #Applies a 20% bulk discount to the order if it contains 5 or more e-books.
        if len(order.get_ebooks()) >= 5: #Check if bulk discount applies
            discount_amount = order.get_total_amount() * 0.20  #20% bulk discount calculates
            order.set_total_amount(order.get_total_amount() - discount_amount) #Apply bulk discount

    # Method to calculate the best discount (either loyalty or bulk) and apply it
    def calculate_final_discount(self, order: Order):
        try:
            # Ensure the order has the necessary methods and attributes
            total_amount = order.get_total_amount() # Get current total amount
            member_discount_amount = order.get_total_amount() * self.__discount #Calculate loyalty discount
            # Apply the greater of the two discounts
            bulk_discount_amount = 0
            if len(order.get_ebooks()) >= 5: #Check if bulk discount applies
                bulk_discount_amount = order.get_total_amount() * 0.20  # 20% bulk discount

            #Apply the greater of the two discounts
            if bulk_discount_amount > member_discount_amount:
                new_total = total_amount - bulk_discount_amount
                order.set_total_amount(new_total)
                print(f"Bulk discount of 20% applied. Total amount after discount: ${new_total}")
            else:
                new_total = total_amount - member_discount_amount
                order.set_total_amount(new_total)
                print(f"Loyalty member discount of {self.__discount * 100}% applied. Total amount after discount: ${new_total}")
        except AttributeError:
            print("Error: Order object missing required attributes.")
        except TypeError:
            print("Error: Invalid type encountered while calculating discount.")
        finally:
            print("Discount calculation complete.")

# String representation of eBook for easy printing
    def __str__(self):
        return super().__str__() + f"\nLoyalty Discount: {self.__discount * 100}%"

#test case
# Test functions
def test_add_modify_remove_ebook():
    print("\n--- Test: Add/Modify/Remove EBook ---")  # Header for this test case
    # Prompting user to enter e-book details for addition
    title = input("Enter e-book title: ")  # Taking title from user
    author = input("Enter author: ")  # Taking author from user
    publication_date = input("Enter publication date (DD-MM-YYYY): ")  # Taking publication_date from user
    genre = input("Enter genre: ")  # Taking genre from user
    price = float(input("Enter price: "))  # Taking price and converting to float

    # Creating an EBook instance independently of any other class
    ebook = EBook(title, author, publication_date, genre, price)  # Creates an eBook instance for testing
    print("EBook added:", ebook)  # Prints the created eBook instance

    # Modifying e-book details with user input
    new_title = input("\nEnter new title to update: ")  # Taking new title for updating
    new_price = float(input("Enter new price: "))  # Taking new price for updating and converting to float
    ebook.set_title(new_title)  # Updates title using the set_title method
    try:
        ebook.set_price(new_price)  # Updates price with validation
    except ValueError as ve:  # Catches ValueError if price is negative
        print(f"Error: {ve}")  # Prints the error message if an invalid price was entered

    print("Updated EBook:", ebook)  # Displays the updated eBook


def test_add_modify_remove_customer():
    print("\n--- Test: Add/Modify/Remove Customer ---") #Header for this test case
    # Prompting user for customer details for addition
    name = input("Enter customer name: ") #Taking customer's name
    email = input("Enter customer email: ") #Taking customer's email
    phone_number = input("Enter customer phone number: ") #Taking customer's phone_number
    address = input("Enter customer address: ") #Taking customer's address

    #Creating a Customer instance independently
    customer = Customer(name, email, phone_number, address) #Creates a Customer instance with entered details
    print("Customer added:", customer) #Displays the created customer details

    #Prompting for updated details
    new_name = input("\nEnter updated name for customer: ")  # Prompt for updated name
    new_email = input("Enter updated email for customer: ")  # Prompt for updated email
    new_phone_number = input("Enter updated phone number for customer: ")  # Prompt for updated phone number
    new_address = input("Enter updated address for customer: ")  # Prompt for updated address

    # Updating the Customer instance with new details
    customer.set_name(new_name)  # Updates name
    customer.set_email(new_email)  # Updates email
    customer.set_phone_number(new_phone_number)  # Updates phone number
    customer.set_address(new_address)  # Updates address

    print("Updated Customer:", customer) #Displays the updated customer info

    # Aggregation between Customer and ShoppingCart
    # A customer can have a shopping cart, but the cart exists independently.
    cart = ShoppingCart() #Creates a ShoppingCart instance
    customer._Customer__cart = cart #Directly setting the cart for demonstration purposes
    print("Shopping cart assigned to customer:", customer._Customer__cart) #Displays assigned cart

    # Removing the Customer by deleting its instance
    del customer  # Deletes customer instance to demonstrate removing the Customer
    print("Customer removed.\n") #Confirms customer removal


def test_shopping_cart_operations():
    print("\n--- Test: Shopping Cart Operations ---") #Header for shopping cart
    #Creates a ShoppingCart instance for testing purposes
    cart = ShoppingCart() #Aggregation with EBook: ShoppingCart contains multiple EBooks

    # Adding e-books to the shopping cart based on user input
    num_items = int(input("How many e-books would you like to add to the cart? ")) #Number of eBooks to add to cart
    for _ in range(num_items): #Looping for the number of items entered by user
        title = input("Enter e-book title: ") #Taking e-book title
        author = input("Enter author: ") #Taking author name
        publication_date = input("Enter publication date (DD-MM-YYYY): ") #Taking publication date
        genre = input("Enter genre: ") #Taking genre
        price = float(input("Enter price: ")) #Taking price and converting to float

        # Creating an EBook instance to add to the cart
        ebook = EBook(title, author, publication_date, genre, price) #Creating an eBook instance
        cart.add_ebook(ebook)  #Adds eBook to ShoppingCart (aggregation)

    print("Shopping Cart Contents:", cart) # Displays items of the shopping cart

    # Removing an item from the shopping cart based on title
    if num_items > 0: #Checks if there are items in the cart to remove
        title_to_remove = input("\nEnter the title of the e-book to remove: ")  #Title of eBook to remove
        for item in cart.get_cart_items(): #Repeat over items in the cart
            if item.get_title() == title_to_remove: #Checks if the title matches user
                cart.remove_ebook(item)  #Removes eBook from ShoppingCart (aggregation)
                print(f"Removed {title_to_remove} from the cart.") #Confirmation message
                break #Breaks loop after removing item
        else:
            print("EBook not found in the cart.") #Message if eBook not found

    print("Final Shopping Cart Contents:", cart) #Displays final shopping cart

def test_discount_application():
    print("\n--- Test: Discount Application ---") #Header for discount application test case
    #Asking user for customer details and loyalty status
    name = input("Enter customer name: ") #Taking customer's name
    email = input("Enter customer email: ") #Taking customer's email
    phone_number = input("Enter customer phone number: ") #Taking customer's phone_number
    address = input("Enter customer address: ") #Taking customer's address
    is_loyalty_member = input("Is the customer a loyalty member? (yes/no): ").strip().lower() == "yes" #Checking loyalty; strip spaces and convert to lowercase for case-insensitive matching

    # Creating a Customer or LoyaltyMember based on loyalty status
    # Inheritance: LoyaltyMember --> Customer
    if is_loyalty_member:
        # Create an instance of LoyaltyMember if the customer is a loyalty member
        customer = LoyaltyMember(name, email, phone_number, address)
    else:
        # Otherwise, create a regular Customer instance
        customer = Customer(name, email, phone_number, address)

    # Adding multiple e-books to apply bulk discount
    num_items = int(input("\nHow many e-books are being purchased? ")) #Number of eBooks for order
    ebooks = [] #List to store eBooks for the order
    for _ in range(num_items): #Looping for each eBook to be added
        title = input("Enter e-book title: ") #Taking e-book title
        author = input("Enter author: ") #Taking e-book author
        publication_date = input("Enter publication date (DD-MM-YYYY): ") #Taking e-book publication_date
        genre = input("Enter genre: ") #Taking e-book genre
        price = float(input("Enter price: ")) #Taking e-book price and converting to float
        ebooks.append(EBook(title, author, publication_date, genre, price)) #Appending eBook to list

    # Creating an Order instance with Customer (composition) and EBooks (aggregation)
    order = Order(1, ebooks, customer)  #Composition with Customer, Aggregation with EBook
    order.apply_discounts()  #Applies loyalty/bulk discounts based on customer type and eBook count
    print(f"Total after applying discounts (if any): ${order.get_total_amount():.2f}") #Displays discounted total


def test_invoice_generation():
    print("\n--- Test: Invoice Generation ---") #Header for invoice generation test case
    #Asking user for customer details and loyalty status
    name = input("Enter customer name: ") #Taking customer's name
    email = input("Enter customer email: ") #Taking customer's email
    phone_number = input("Enter customer phone number: ") #Taking customer's phone_number
    address = input("Enter customer address: ") #Taking customer's address
    is_loyalty_member = input("Is the customer a loyalty member? (yes/no): ").strip().lower() == "yes" #Checking loyalty; strip spaces and convert to lowercase for case-insensitive matching

    # Creating a Customer or LoyaltyMember based on loyalty status
    # Inheritance: LoyaltyMember --> Customer
    if is_loyalty_member:
        # Create an instance of LoyaltyMember if the customer is a loyalty member
        customer = LoyaltyMember(name, email, phone_number, address)
    else:
        # Otherwise, create a regular Customer instance
        customer = Customer(name, email, phone_number, address)

    # Adding multiple e-books to the order
    num_items = int(input("\nHow many e-books are being ordered? ")) #Number of eBooks for order (Customer, etc)
    ebooks = [] #List to store eBooks for the order
    for _ in range(num_items): #Looping for each eBook to be added
        title = input("Enter e-book title: ") #Taking title
        author = input("Enter author: ") #Taking author
        publication_date = input("Enter publication date (DD-MM-YYYY): ") #Taking publication date input
        genre = input("Enter genre: ") #Taking genre
        price = float(input("Enter price: ")) #Taking price and converting to float
        ebooks.append(EBook(title, author, publication_date, genre, price)) #Appending eBook to list

#Creating an Order instance with Customer (composition) and EBooks (aggregation)
    order = Order(1, ebooks, customer) #Composition with Customer, Aggregation with EBook
    payment = Payment(order) #Composition between Payment and Order

    # Generate and print invoice
    print("\nInvoice generated:") #Header for generated invoice
    print(payment.generate_invoice(order)) #Prints generated invoice with itemized details


# Run test cases
if __name__ == "__main__":
    # Running each test case to demonstrate system functionality
    test_add_modify_remove_ebook() #Tests adding, modifying, and removing an eBook
    test_add_modify_remove_customer() #Tests adding, modifying, and removing a Customer, with aggregation of ShoppingCart
    test_shopping_cart_operations() #Tests adding and removing eBooks in a ShoppingCart
    test_discount_application() #Tests applying discounts for LoyaltyMember or bulk purchase
    test_invoice_generation() #Tests generation of an invoice including discounts and VAT