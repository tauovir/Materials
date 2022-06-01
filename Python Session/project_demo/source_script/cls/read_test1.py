

def read_test():
    print("==========")
    path = r"C:\Users\LENOVO\Desktop\Materials\Python Session\project_demo\source_script\cls\output\file1.txt"
    path = r"C:\Users\LENOVO\Desktop\Materials\Python Session\project_demo\source_script\cls\output\readpy.py"
    fileobject = None
    try:
        fileobject = open(path)
        print(fileobject.read(20))

        # print(fileobject.readline())
        # print(fileobject.readline())
        # print(fileobject.readline(30))
        # print(fileobject.readlines(2))
        # print(fileobject.readlines(2))
        # print(fileobject.readlines(5))
        # print("tell:", fileobject.tell())  ## get the current file position
        # print(fileobject.read(20))
        # print("tell:", fileobject.tell())
        # print("tellend:", fileobject.seek(2))
        # print(fileobject.read(20))
        fileobject.flush()
        print("======================end===")
        print(fileobject.read())
    except FileNotFoundError:
        print(f"File:{path} not found")
    finally:
        if fileobject:
            fileobject.close()

    print("Program end")


def write_file():
    path = r"C:\Users\LENOVO\Desktop\Materials\Python Session\project_demo\source_script\cls\output\writepy3.txt"
    fileobject = None
    try:
        with open(path,"r+") as fileobject:
            str = """khan is here102030"""
            # print(fileobject.read())
            print(fileobject.write(str))
    except FileNotFoundError:
        print("File not found")
    finally:
        if fileobject:

            fileobject.close()



def read101():
    path = r"C:\Users\LENOVO\Desktop\Materials\Python Session\project_demo\source_script\cls\output\writepy3.txt"
    fileobject = None
    try:
        with open(path,"w") as fileobject:
            pass
            # str = """khan is here102030"""
            # print(fileobject.read(10))
            # fileobject.seek(50)
            # print(fileobject.read(10))
    except FileNotFoundError:
        print("File not found")
    finally:
        if fileobject:

            fileobject.close()

def binary():
    path = r"C:\Users\LENOVO\Desktop\Materials\Python Session\project_demo\source_script\cls\output\bnrw.bn"
    fileobject = None
    try:
        with open(path, "wb") as fileobject:
            fileobject.write('Hello World'.encode())


    except FileNotFoundError:
        print("File not found")
    finally:
        if fileobject:
            fileobject.close()



if __name__ =="__main__":
    # read_test()
    binary()
