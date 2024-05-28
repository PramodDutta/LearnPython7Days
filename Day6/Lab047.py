class GrandFather:
    def bhk(self):
        print("0BHK")
        
    def lambo(self):
        print("Driving Lambo")

class Father(GrandFather):
    def bhk(self):
        print("1BHK")


class Son(Father):
    def bhk(self):
        print("2BHK")


s = Son()
s.bhk()
s.lambo()