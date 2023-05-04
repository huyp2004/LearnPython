class Student:
    count = 0

    def __init__(self, name, id, old):
        self.name = name
        self.id = id
        self.old = old
        Student.count += 1

    def get_id(self):
        return self.id

    def set_name(self):
        self.name
    
    def get_name(self):
        return self.name
    
    def show(self):
        print('Ho va ten:', self.get_name())
        print('Nam Sinh:', self.old)
        print('MSSV:', ())



