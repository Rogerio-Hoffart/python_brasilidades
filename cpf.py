
class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.valida_cpf(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!!")

    def __str__(self):
        return  self.formata_cpf()

    def valida_cpf(self, documento):
        if len(documento) == 11:
            return True
        else:
            return False

    def formata_cpf(self):
        cjto1 = self.cpf[:3]
        cjto2 = self.cpf[3:6]
        cjto3 = self.cpf[6:9]
        cjto4 = self.cpf[9:]
        return "{}.{}.{}-{}".format(cjto1, cjto2, cjto3, cjto4)
