#!/usr/bin/env python3
import unittest
class Complejo(object):
    def __init__(self,real,imag=0):
        self.real = real
        self.imag = imag

    def sumar(self, otro):
        result = Complejo(self.real + otro.real, self.imag + otro.imag)
        return result
    def restar (self,otro):
        result = Complejo(self.real - otro.real, self.imag - otro.imag)
        return result
    def multiplicar(self,otro):
        result = Complejo(self.real * otro.real - self.imag * otro.imag, self.real * otro.imag + self.imag * otro.real)
        return result
    def dividir(self, otro):
        modulo = otro.real ** 2 + otro.imag ** 2
        result = Complejo((self.real * otro.real + self.imag * otro.imag)/modulo, (self.imag * otro.real - self.real * otro.imag)/modulo)
        return result
    def igual (self,otro):
        return self.real == otro.real and self.imag == otro.imag

class TestComplejo(unittest.TestCase):

    def test_sumar(self):

        c1 = Complejo(1,2)
        c2 = Complejo(3,4)

        suma = c1.sumar(c2)

        self.assertEqual(suma.real, 4)
        self.assertEqual(suma.imag, 6)

    def test_restar(self):

        c1 = Complejo(6,1)
        c2 = Complejo(8,4)

        resta = c1.restar(c2)

        self.assertEqual(resta.real, -2)
        self.assertEqual(resta.imag, -3)

    def test_restar_malo(self):   #Compruebo a posta que está mal

        c1 = Complejo(6,1)
        c2 = Complejo(8,4)

        resta = c1.restar(c2)

        self.assertEqual(resta.real, -1)
        self.assertEqual(resta.imag, -5)

    def test_multiplicar(self):
        c1 = Complejo(-1,1)
        c2 = Complejo(2,1)

        multiplica = c1.multiplicar(c2)

        self.assertEqual(multiplica.real,-3)
        self.assertEqual(multiplica.imag,1)

    def test_dividir(self):
        c1 = Complejo(-1,1)
        c2 = Complejo(2,1)

        divide = c1.dividir(c2)

        self.assertEqual(divide.real,-1/5)
        self.assertEqual(divide.imag, 3/5)


if __name__ == "__main__":
    unittest.main()
