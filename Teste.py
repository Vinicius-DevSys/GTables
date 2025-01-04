from GTables import *

# Montagem da tabela.
CSV = TableMaker(["Nome", "Idade", "CPF"])
CSV.add_row(["James", 22])
CSV.add_row(["Mary", 18])
CSV.add_row(["George", 25])

# Trecho para nos ajudar a visualizar o estado da tabela.
for i in CSV.check_table():
    print(i)

# Exportação da tabela em arquivo csv.
CSV.build()
