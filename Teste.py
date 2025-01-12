from GTables import *

# Elementos para composição dos dados.
subst = ["Espada", "Escudo", "Lança", "Adaga", "Orb", "Martelo"]
adject = ["de Fogo", "Congelante", "Lendária", "Ancestral", "das Sombras", "de Guerra"]

# Montagem da tabela.
CSV = TableMaker(["Item", "Valor"])
MOCK = DataMaker(subst, adject, last_number=100)

# Geração de dados.
for i in range(10):
    CSV.add_row([MOCK.create_name_data(), MOCK.create_progress_data([15, 35])])

# Exportação da tabela em arquivo csv.
CSV.build()
