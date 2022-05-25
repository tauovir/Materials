
class Employee:

    type = "RDW Employee"

    def __init__(self,name, age, salary):
        print("I am going to initialized")

        self.name = name   # instance attribute
        self.age = age
        self.salary = salary
        print(self.salary)


    def show_me(self):
        """
        instance method
        :return:
        """
        self.add_incentive()
        print(f"My name is {self.name}, I am {self.age} old, I am getting {self.salary}")

    def add_incentive(self):
        """
        instance method
        :return:
        """
        self.salary = self.salary  +500

    def show_cls(self):
        print("employee type self:",self.type)
        print("employee type class:",Employee.type)




if __name__ == "__main__":

    obj = Employee(name="Rahul", age=25, salary=250000)
    obj.show_me()
    obj.type = "Some type"
    obj.show_cls()
    print("==============")
    print(Employee.type)


    obj1 = Employee(name="Amit", age=26, salary=21000)
    obj1.show_me()
    obj.show_cls()
    import datetime
    print(datetime.date.today())
