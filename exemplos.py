from telefones_br import TelefonesBr
import re
from cpf_cnpj import Documento
from datetime import datetime, timedelta
from date_time import DateTime


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

teste_objeto = '551523462456'
meu_numero = TelefonesBr(teste_objeto)
print(meu_numero)

data_cadastro = DateTime()
print(data_cadastro)
print(data_cadastro.mes_cadastro())
print(data_cadastro.dia_semana())
print(data_cadastro.tempo_cadastro())

hoje = datetime.today()
amanha = datetime.today() + timedelta(days=2, hours=5, minutes=30)

print(amanha - hoje)


