class Rectangle:
    def __init__(self, length, width):
        if not length:
            raise ValueError("Missing length")
        if not width:
            raise ValueError("Missing width")

        self.length = length
        self.width = width

    def perimeter(self):
        return (self.length + self.width) / 2

    def acreage(self):
        return (self.length * self.width)

rect = Rectangle(10, 5)
print("Chu vi của hình chữ nhật là:", rect.perimeter())
print("Diện tích của hình chữ nhật là:", rect.acreage())
