
class Customer():
    def __init__(self,customer_id,last_name,first_name,phone_number, address):
        if not isinstance(customer_id, int):
            raise TypeError("Customer ID must be set to an integer")
        else:
            self.customer_id = customer_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.address = address

    def change_customer_id(self, customer_id):
        if not isinstance(customer_id, int):
            raise TypeError("Customer ID must be set to an integer")
        else:
            self.customer_id = customer_id

    def change_last_name(self, last_name):
        self.last_name = last_name

    def change_first_name(self, first_name):
        self.first_name = first_name

    def change_phone_number(self,phone_number):
        self.phone_number = phone_number

    def change_address(self, address):
        self.address = address

    def __repr__(self):
        return "{}".format(self.address)

    def __str__(self):
        return "{}{}".format(self.first_name,self.last_name)

    def display(self):
        return "Customer ID: {} \nCustomer Name: {},{}\nCustomer Phone: {}\nCustomer Address: {}".format(self.customer_id,self.last_name,self.first_name,self.phone_number,self.address)



customer1 = Customer(4,"Hobbs","Ty","3193309818", "123 Main St")
print(customer1.display())
print(customer1)
# customer2 = Customer("z","Hobbs","Ty","3193309818", "address")
# print(customer2.display())



