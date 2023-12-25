class Student:
    def __init__(self, name, address):
        if not name:
            raise ValueError("Missing Name")
        # if address not in ['An Phu', 'Binh Duong', 'TP. HCM']:
        #     raise ValueError("Invalid Address")

        self.name = name
        self.address = address


def main():
    student = get_student()
    print(f"Name: {student.name} form {student.address}")


def get_student():
    name = input("Enter Name: ")
    address = input("Address: ")
    return Student(name, address)


if __name__ == "__main__":
    main()
