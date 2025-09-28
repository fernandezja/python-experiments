import unittest
from calculadora import Calculadora

class CalculadoraTest(unittest.TestCase, Calculadora):

    def test_restar_3menos2_devuelve1(self):
        calc = Calculadora()
        resultado = calc.restar(3, 2)
        self.assertEqual(1, resultado)

    def test_restar_10menos9_devuelve1(self):
        calc = Calculadora()
        resultado = calc.restar(10, 9)
        self.assertEqual(1, resultado)

    def test_restar_10menos5_devuelve5(self):
        calc = Calculadora()
        resultado = calc.restar(10, 5)
        self.assertEqual(5, resultado)

    # def test_restar_dosValores_devuelveResultado(self):
    #     calc = Calculadora()
    #     resultado = calc.restar(3, 2)
    #     self.assertEqual(1, resultado)

    def test_edad_siNacio08091994_debeTener23anios(self):
        calc = Calculadora()
        resultado = calc.edad(8,9,1994)
        self.assertEqual(23, resultado)

    def test_edad_siNacio01101990_debeTener27anios(self):
        calc = Calculadora()
        resultado = calc.edad(1,10,1990)
        self.assertEqual(27, resultado)

    def test_edad_siNacio11051994_debeTener23anios(self):
        calc = Calculadora()
        resultado = calc.edad(11,5,1994)
        self.assertEqual(23, resultado)