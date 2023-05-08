import re
from telefones_br import TelefonesBr
from cpf_cnpj import Documento

cpf = '12354367996'

cnpj = '35379838000112'

documento = Documento.cria_documento(cnpj)

print(documento)

documento1 = Documento.cria_documento(cpf)

print(documento1)
#---------------------------------------------
padrao = "[0-9][a-z][0-9]"
texto = '123 1bc z3a 4d2 rer 5f3'
busca = re.findall(padrao, texto)

print(busca)

padrao = "\w{5,50}@[a-z]{3,10}.com.br"
texto = '123 1bc josewilson@yahoo.com.br 4d2 rer 5f3'
busca = re.search(padrao, texto)

print(busca.group())

padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
texto = '123 1bc z3a 15934562361 4d2 rer 5f3'
busca = re.search(padrao, texto)

print(busca.group())

teste_objeto = "551523463452"
meu_numero = TelefonesBr(teste_objeto)
print(meu_numero)
