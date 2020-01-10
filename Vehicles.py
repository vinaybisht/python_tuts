
class Vehicles:

    def __init__(self, name="", age=0, owner=""):
        self._name = name
        self._age = age
        self._owner = owner

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def set_owner(self, owner):
        self._owner = owner

    def get_owner(self):
        return self._owner

    def get_age(self):
        return self._age

    def get_name(self):
        return self._name


vehicles = Vehicles()
vehicles.set_age(50)
vehicles.set_name("Maruti Suzuki")
vehicles.set_owner("Vinay singh bisht")
print("Name of Vehicle %s" % vehicles.get_name())
print("Age of cars %s" % vehicles.get_age())

