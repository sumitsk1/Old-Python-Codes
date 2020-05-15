# c# will discuss three problems in existing
# then we will solve them using getter , setter decorator


class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price, 0)
        # self.complete_specification = f"{self.brand} {self.model_name} and price is {self._price}"

    @property
    def complete_specification(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"

    # getter() , setter()

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = max(new_price, 0)

    def make_a_call(self, phone_number):
        print(f"calling {phone_number} ...")

    def full_name(self):
        return f"{self.brand} {self.model_name}"


phone1 = Phone('Nokia', '1100', 1000)

phone1.price = -500
print(phone1.price)
print(phone1.complete_specification)

####################################################################################

# class Phone:
#     def __init__(self,brand,model_name,price):
#         self.brand=brand
#         self.model_name=model_name
#         self.price=price
#         self.full_specs=f"{self.brand} {self.model_name} and {self.price}"
#
#     def make_a_call(self,number):
#         print(f'calling....{number}')
#
#     def full_name(self):
#         return f"{self.brand} {self.model_name}"
#
#
#
#