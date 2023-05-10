from datetime import datetime, timedelta

class DateTime:
    def __init__(self):
        self.data_cadastro = datetime.today()

    def __str__(self):
        return self.formata_data()

    def mes_cadastro(self):
        meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
        mes_cadastro = self.data_cadastro.month - 1
        return meses[mes_cadastro]

    def dia_semana(self):
        dias = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']
        dia_cadastro = self.data_cadastro.weekday()
        return dias[dia_cadastro]

    def formata_data(self):
        data_formatada = self.data_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=80, hours=800)) - self.data_cadastro
        return tempo_cadastro