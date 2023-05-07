from cpf_cnpj import Documento

cpf = '12354367996'

cnpj = '35379838000112'

documento = Documento.cria_documento(cnpj)

print(documento)

documento1 = Documento.cria_documento(cpf)

print(documento1)