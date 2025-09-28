import datetime

class Calculadora():

    def sumar(self, x, y):
        return x+y

    def restar (self, x, y):
        return x-y

    def edad (self, dia, mes, anio):
        diaNac = datetime.date(anio,mes, dia)
        hoy = datetime.date.today()
        resultado = hoy-diaNac
        return int(resultado.days / 365)