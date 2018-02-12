# Decorator function to put phone numbers in a proper format

class PhoneBook(object):
    def __init__(self):
        self.phone_num_list = []

    def phone_num_decorator(**kwargs2):

        def modified_fun(*args, **kwargs):
            #import pdb;pdb.set_trace()
            print("country is "+str(kwargs2["country"]))
            if kwargs["country"]=="us":
                func(self, "+1-"+str(num))

    @phone_num_decorator(country="us")
    def add_phone_to_list(self, num):
        self.phone_num_list.append(num)

    def print_phonebook(self):
        for num in self.phone_num_list:
            print(num)


p = PhoneBook()
p.add_phone_to_list("9962515151")
p.add_phone_to_list("9962515152")
p.add_phone_to_list("9962515153")
p.print_phonebook()


