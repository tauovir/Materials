

class ReadFile:


    def readfile(self):
        path = r"C:\Users\LENOVO\Desktop\Materials\Python Session\project_demo\output\file1.txt"
        fileobject = None
        try:
            fileobject = open(path,"w")
            print(fileobject.read())
            # print("After reading file")
            # print(fileobject.tell())
            fileobject.seek(5)
            # print(fileobject.read(50))
            # print(fileobject.readline())
            # print(fileobject.readline())
            # print(fileobject.readlines())
        except FileNotFoundError:
            print("Fine  not found")
        finally:
            if fileobject:
                fileobject.close()

    def writefile(self):
        path = r"C:\Users\LENOVO\Desktop\Materials\Python Session\project_demo\output\output.txt"
        fileobject = None
        try:
            msg = "###########"
            fileobject = open(path, "+r")
            fileobject.seek(0)
            print(fileobject.write(msg))

        except FileNotFoundError:
            print("Fine  not found")
        finally:
            if fileobject:
                fileobject.close()






    def read_file(self):

        """
        f = open("test.txt", mode='r', encoding='utf-8')
        Moreover, the default encoding is platform dependent. In windows, it is cp1252 but utf-8 in Linux.
        :return:
        """

        path = r"C:\Users\LENOVO\Desktop\Materials\Python Session\project_demo\source_script\cls\output\file1.txt"
        fileobject = None
        try:
            fileobject = open(path, encoding='utf-8')
            print(fileobject.read(10))  # read the first 4 data

            # content = fileobject.read()  # read in the rest till end of file
            # print(content)
            # content2 = fileobject.read()  ## further reading returns empty sting
            print("tell",fileobject.tell())  ## get the current file position
            print(fileobject.read(10))
            fileobject.seek(0)  # # bring file cursor to initial position
            print("seek tell", fileobject.tell())
            print(fileobject.read(10))
        except Exception as e1:
            raise (e1)
        finally:
            if fileobject:
                print("Closed")
                fileobject.close()

    def read_file_line(self):
        """
        We can read a file line-by-line using a for loop. This is both efficient and fast.
        :return:
        """
        path = r"C:\Users\LENOVO\Desktop\Materials\Python Session\project_demo\source_script\cls\output\file1.txt"
        fileobject = None
        try:
            fileobject = open(path, encoding='utf-8')
            # for line in fileobject:
            #     # print(line)
            #     pass

            """
            Alternatively, we can use the readline() method to read individual lines of a file. 
            This method reads a file till the newline, including the newline character
            """
            print(fileobject.readline())
            # print("=======")
            print(fileobject.readline())
            """
            Lastly, the readlines() method returns a list of remaining lines of the entire file. 
            All these reading methods return empty values when the end of file (EOF) is reached.
            """
            print(fileobject.readlines())

        except Exception as e1:
            raise (e1)
        finally:
            if fileobject:
                fileobject.close()

    def read_file_with(self):
        """"
        The with statement automatically takes care of closing the file once it leaves the with block,
        even in cases of error. I highly recommend that you use the with statement as much as possible,
        as it allows for cleaner code and makes handling any unexpected errors easier for you.
        """

        path = r"C:\Users\LENOVO\Desktop\Materials\Python Session\project_demo\output\file1.txt"

        with open(path) as fileobject:
            print(fileobject.read())
            print(fileobject.readline())

    def read_and_writefile(self):
        read_file = r"C:\Users\LENOVO\Desktop\Materials\Python Session\project_demo\output\file1.txt"
        write_file = r"C:\Users\LENOVO\Desktop\Materials\Python Session\project_demo\output\write101.txt"
        fileobject = None
        try:
            with open(read_file, encoding='utf-8') as readobj, open(write_file, 'a', encoding='utf-8') as writeobj:
                data = readobj.readlines()
                writeobj.writelines(data)

        except Exception as e1:
            raise (e1)
        finally:
            if fileobject:
                print("Closed")
                fileobject.close()

    def write_file(self):
        """
        .write(string)	This writes the string to the file.
        .writelines(seq)	This writes the sequence to the file.
        No line endings are appended to each sequence item.
        It’s up to you to add the appropriate line ending(s).

        :return:
        """
        path = r"C:\Users\LENOVO\Desktop\Materials\Python Session\project_demo\source_script\cls\output\wfile1.txt"
        fileobject = None
        try:
            with open(path, "a") as fileobject:
                # fileobject.write("Hi there")
                # fileobject.write("Writeing seconf line")
                fileobject.writelines("Writeing seconf line")
                fileobject.writelines("Writeing seconf line 10203000000")
        except Exception as e1:
            raise (e1)

    def read_and_write(self):
        read_file = r"C:\Users\LENOVO\Desktop\Materials\Python Session\project_demo\source_script\cls\output\file1.txt"
        write_file = r"C:\Users\LENOVO\Desktop\Materials\Python Session\project_demo\source_script\cls\output\wfile1.txt"
        fileobject = None
        try:
            with open(read_file, encoding='utf-8') as fileobject:
                data = fileobject.readlines()

            with open(write_file,'w',encoding='utf-8') as writeobj:
                for line in data:
                    writeobj.writelines(line)


        except Exception as e1:
            raise (e1)
        finally:
            if fileobject:
                print("Closed")
                fileobject.close()

    def read_and_write2(self):
        read_file = r"C:\Users\LENOVO\Desktop\Materials\Python Session\project_demo\source_script\cls\output\file1.txt"
        write_file = r"C:\Users\LENOVO\Desktop\Materials\Python Session\project_demo\source_script\cls\output\wfile1.txt"
        fileobject = None
        try:
            with open(read_file, encoding='utf-8') as readobj,open(write_file, 'a', encoding='utf-8') as writeobj:
                data = readobj.readlines()
                writeobj.writelines(data)

        except Exception as e1:
            raise (e1)
        finally:
            if fileobject:
                print("Closed")
                fileobject.close()

    def read_and_write23(self):
        read_file = r"C:\Users\LENOVO\Desktop\Materials\Python Session\project_demo\source_script\cls\output\file12.txt"
        fileobject = None
        try:
            with open(read_file, "x",encoding='utf-8') as readobj:
                readobj.write("Mangoooo")



        except Exception as e1:
            raise (e1)
        finally:
            if fileobject:
                print("Closed")
                fileobject.close()


if __name__ =="__main__":
    # ReadFile().readfile()
    # ReadFile().writefile()
    # ReadFile().read_file_with()
    ReadFile().read_and_writefile()
