from docassemble.base.util import Individual

class Pareja(Individual):
    def init(self, *pargs, **kwargs):
        super().init(*pargs, **kwargs)
    def summary(self):
        return "Esta persona es pareja del individuo principal de la parte"