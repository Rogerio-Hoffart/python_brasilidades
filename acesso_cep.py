import requests
import re

class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.cep_eh_valido(cep):
            self.cep = cep
        else:
            raise ValueError ("CEP inválido!!")

    def __str__(self):
        return self.formata_cep()

    def cep_eh_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def formata_cep(self):
        padrao = "([0-9]{5})([0-9]{3})"
        resposta = re.search(padrao, self.cep)
        cep_formatado = "{}-{}".format(resposta.group(1), resposta.group(2))
        return cep_formatado

    def acessa_via_cep(self):
        url = 'https://viacep.com.br/ws/{}/json/'.format(self.cep)
        r = requests.get(url)
        return r.text