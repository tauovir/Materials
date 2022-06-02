import csv

class ReadCsv:

    read_file = r"C:\Users\LENOVO\Desktop\Materials\Python Session\project_demo\data_dir\user_data.csv"
    write_file = r"C:\Users\LENOVO\Desktop\Materials\Python Session\project_demo\data_dir\write_users101.csv"
    def read_csv(self):

        """

        To read a CSV file in Python, we can use the csv.reader()
        :return:
        """
        user_data = []
        with open(ReadCsv.read_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            line_count = 0
            columns = []
            for row in csv_reader:
                line_count += 1
                if line_count==1:
                    columns = row
                    continue
                dict1 = dict(zip(columns,row))
                print(dict1)
                user_data.append(row)

            return user_data

    def read_csv_dict(self):
        user_data = []

        with open(ReadCsv.read_file) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')

            for row in csv_reader:
                print("row:",row)
                user_data.append(row)
            return user_data

    def write_csv(self):
        """
        To write to a CSV file in Python, we can use the csv.writer() function.
        :return:
        """
        user_data = []
        with open(ReadCsv.write_file, mode='a') as employee_file:
            employee_writer = csv.writer(employee_file, delimiter='|')
            employee_writer.writerow(['John Smith', 'Accounting', 'November'])
            employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
            employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
            employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
            employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

        print("==========End up===")

    def write_csv2(self):

        import datetime as dt
        with open(ReadCsv.write_file, mode='w',newline = '' ) as csv_file:
            fieldnames = ["id","name","mobile","salary","created_at"]   #column name
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            data = [
                {"id" : "101","name" : "APPLE","mobile" : "99365842","salary" : 152014,
                 "created_at": dt.datetime.today().strftime("%Y-%m-%d")},
                {"id": "102", "name": "Mango", "mobile": "15896312", "salary": 25482,
                 "created_at": dt.datetime.today().strftime("%Y-%m-%d")},
                {"id": "103", "name": "Banan", "mobile": "98745123", "salary": 25600,
                 "created_at": dt.datetime.today().strftime("%Y-%m-%d")}
            ]
            writer.writeheader()
            for row in data:
                writer.writerow(row)


if __name__ =="__main__":
    x = ReadCsv().write_csv2()
    # x = ReadCsv().read_csv_dict()
    # ReadCsv().write_csv()
    # ReadCsv().write_csv2()
