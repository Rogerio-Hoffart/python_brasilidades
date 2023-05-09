from datetime import datetime, timedelta

class DateTime:
    def __init__(self):
        self.data_cadastro = datetime.today()

    def mes_cadastro(self):
        meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
        mes_cadastro = self.data_cadastro.month - 1
        return meses[mes_cadastro]

    def dia_semana(self):
        dias = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']
        dia_cadastro = self.data_cadastro.weekday()
        return dias[dia_cadastro]