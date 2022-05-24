
from service.aws_services import upload_file,remove_file
from helper.common_helper import display_msg
def main():

    upload_file("s3_file")
    remove_file("s3_file")
    print("Main function is calling")
    print(display_msg())



if __name__ == "__main__":
    main()
