
class BaseClass:
    title = "Centeral University"
    cnt = 0

    def __init__(self,name,city,fund ):
        self.name = name
        self.city = city
        self.__fund = fund
        self.country = "India"
        BaseClass.cnt +=1


    def display(self):
        print(f"name:{self.name},location :{self.city}")

    def show(self):
        self.display()
        # self.class_method() # not accessible

    @classmethod
    def class_method(cls):
        print("Class method")
        print("Number of object created.",cls.cnt)
        # print(cls.display()) # cannot access instance variable/method
        print(BaseClass.title)


if __name__ =="__main__":
    obj = BaseClass(name = "Medical college",city="delhi",fund=5000)
    obj3 = BaseClass(name="Medical college2", city="delhi2",fund=15000)
    # print(obj3._fund)
    # print(vars(obj3))  # attribute and values
    # print(dir(obj3))   # attribute and internal method
    # print(vars(BaseClass))
    # print("===========")
    # print(dir(BaseClass))
