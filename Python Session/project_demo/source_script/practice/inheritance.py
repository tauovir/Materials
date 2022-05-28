
# multi level inheritance
# multipl inheritance


class B2:
    pass

class BaseClass:

    def __init__(self,name):
        self.name = name

    def show_me(self):
        print(f"I am in base class, name:{self.name}")


class DerivedCls(BaseClass,B2):

    def __init__(self,name, derived_name):
        super().__init__(name)
        self.derived_name = derived_name

    def display(self):
        print(f"data name :{self.name},derived : {self.derived_name}")





if __name__ =="__main__":
    obj = DerivedCls(name = "Parent name2",derived_name  = "Child name2")
    obj.display()


1: single type in heritance


