


class Demo:
    type = "Carr"
    def __init__(self, name, age):
        print("Object initialize")
        self.name = name
        self.age = 25

    def show(self):
        self.price = 500


    def display(self):

        print(f"My name is {self.name} and age is {self.age}, price ={self.price}")

    @classmethod
    def cls_method(cls):
        print(type(cls))
        print("class methos")
        print(Demo.type)




if __name__ =="__main__":
    obj = Demo(name = "Khan",age = 60)
    obj.show()
    # print(dir(obj))
    # print("=============Class======")
    # print(dir(Demo))
    obj.display()
    Demo.cls_method()
