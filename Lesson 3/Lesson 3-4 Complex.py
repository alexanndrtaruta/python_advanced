class ComplexNumber:

    def __init__(self, real, img):
        self.real = real
        self.img = img


    def __repr__(self):
        if self.img < 0:
            return '{}{}i'.format(self.real ,self.img)
        else:
            return '{}+{}i'.format(self.real ,self.img)

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.img + other.img)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.img - other.img)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.img * other.img, self.img * other.real + self.real * other.img)

    def __truediv__(self, other):
        x = self.real * other.real + self.img * other.img
        y = self.img * other.real - self.real * other.img
        z = other.real ** 2 + other.img ** 2
        real = x / z
        imag = y / z
        return ComplexNumber(real, imag)

A = ComplexNumber(1, 1)
B = ComplexNumber(2, 3)
print(complex(1, 1)*complex(2, 3))
print(complex(1, 1)/complex(2, 3))
print(A/B)