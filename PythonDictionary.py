# Python dictionary example


class PhoneBook:

    def __init__(self):
        pass

    def _contacts_book(self):
        return {"John": "+91 1234567890",
                "Ron": "+91 0235687900",
                "Xian": "+91 2035689782"}


phone_book = PhoneBook()
local_contacts = phone_book._contacts_book()
print(local_contacts)

local_contacts["John"] = "+910000000000"
print("//Updated value of key John//")
print(local_contacts)

del local_contacts["Xian"]
print("//Deleted Xian from dictionary//")
print(local_contacts)

local_contacts["Remo"] = "+1 6898789502"
print("//Added Remo to dictionary//")
print(local_contacts)

print("//Printing a value from key//")
print(local_contacts["John"])

print("//Printing key and Values of dictionary//")
for key, value in local_contacts.items():
    print(value)
