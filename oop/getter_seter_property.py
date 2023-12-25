class Nguoi:
    def __init__(self, fname, lname, scores: int):
        self.__fname = fname
        self.__lname = lname
        self.__scores = scores

    def set_fname(self, fname):
        self.__fname = fname

    def get_fname(self):
        return self.__fname

    def set_lname(self, lname):
        self.__lname = lname

    def get_lname(self):
        return self.__lname

    def get_name(self):
        return f"{self.__lname} {self.__fname}"

    def set_scores(self, scores):
        self.__scores = scores

    def get_scores(self):
        return self.__scores

    first_name = property(get_fname, set_fname)
    last_name = property(get_lname, set_lname)
    name = property(get_name)
    scores = property(get_scores)


person = Nguoi('Huy', 'Phan Nguyen Quoc', 95)

print("Ho va ten:", person.name)
print("Diem tong ket:", person.scores)
