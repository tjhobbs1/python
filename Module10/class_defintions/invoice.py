class Invoice():
    def __init__ (self,invoice_id,customer_id,last_name,first_name,phone_number,address, item_with_price={}):
        self.invoice_id = invoice_id
        self.customer_id = customer_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone = phone_number
        self.address = address
        self.item_with_price = item_with_price


    def set_invoice_id(self,invoice_id):
        self.invoice_id = invoice_id

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def set_last_name(self,last_name):
        self.last_name = last_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_phone_number(self, phone):
        self.phone = phone

    def set_address(self, address):
        self.address = address

    def add_item(self,item, price):
        self.item_with_price.update({item : price})

    def display(self):
        return "Invoice ID: {}\nCustomer ID:{}\nName: {},{}\nPhone: {}\nAddress: {}\n".format(self.invoice_id, self.customer_id, self.last_name, self.first_name, self.phone, self.address)

    def print_invoice(self):
        for(key, value) in self.item_with_price.items():
            print(key, ": " ,value)


customer1 = Invoice(123,456,"Hobbs","Ty","515-667-8976","123 Main St")
print(customer1.display())
customer1.add_item("Iphone",199)
customer1.print_invoice()





