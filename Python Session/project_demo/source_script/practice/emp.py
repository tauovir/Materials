
class Employee:

    type = "RDW Employee"  # class variable

    def __init__(self,name, age, salary):
        """
        instance variable
        :param name:
        :param age:
        :param salary:
        """

        self.name = name  # public access
        self._age = age   # protected member
        self.__salary = salary   # Private member



    def show_me(self):
        """
        instance method
        :return:
        """
        self.add_incentive()
        print(f"My name is {self.name}, I am {self._age} old, I am getting {self.__salary}")

    def add_incentive(self):
        """
        instance method
        :return:
        """
        self.__salary = self.__salary  +500

    @classmethod
    def class_method(cls):
        print(type(cls))
        print(" I am i class method")





if __name__ == "__main__":

    obj = Employee(name="Rahul", age=25, salary=250002)

    # obj.show_me()
    # print(obj.__salary)
    obj.class_method()






    # Employee.class_method()
    #vars, dir

    # print(vars(obj))
    # print(vars(Employee))
    # print(dir(obj))
    # print(dir(Employee))
