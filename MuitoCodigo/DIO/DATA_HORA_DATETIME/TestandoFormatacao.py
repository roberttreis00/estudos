from datetime import datetime
import re

data_atual = datetime.today().strftime("%A/%m/%y")
quarta = re.compile('Wednesday/')
if re.search(quarta, data_atual):
    print(data_atual.replace('Wednesday', 'Quarta-Feira'))
