class BaseClass:
    title = "Centeral University"
    cnt = 0

    def __init__(self, name, city, fund):
        print("Base class initialize")
        self.name = name
        self._city = city
        self.__fund = fund
        self.country = "India"
        BaseClass.cnt += 1

    def display(self):
        print(f"name:{self.name},location :{self._city},fund:{self.__fund}")

    @classmethod
    def class_method(cls):
        print("Class method")
        print("Number of object created.", cls.cnt)
        # print(cls.display()) # cannot access instance variable/method
        print(BaseClass.title)


class DerivedCls(BaseClass):

    def __init__(self, name, city, fund, derived_name):
        "This should initialize else base property would not be created, object cant be counted",
        super().__init__(name, city, fund)
        self.child_name = derived_name

    def show(self):
        # print(f"name{self.child_name},parent name:{self.name},city:{self._city}")
        super().display()
        # print(f"name{self.__fund}") # not accessible
    def display(self):
        print(" I am there")

    @classmethod
    def class_method(cls):
        print("My class method")

if __name__ == "__main__":
    # obj = BaseClass(name="Medical college", city="delhi", fund=5000)
    obj2 = DerivedCls(name="Medical college", city="delhi", fund=5000,derived_name = "Meerut Ins")
    obj2.display()
    DerivedCls.class_method()
    print()
