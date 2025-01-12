# GTables 1.0.0 - Gerador-de-Tabelas-CSV
> ### <img src="https://github.com/Vinicius-DevSys/GTables/blob/master/Referencias/python.png" width="55" alt="Descrição da imagem"> Conteúdo: Python, CSV, LibreOffice, SGBD, SOLID.

Esse é um módulo para te auxiliar a criar tabelas simples em CSV para você usar no seu banco de dados, LibreOffice ou onde mais você desejar.

## Descrição
Esse módulo serve para você implementar códigos que trabalhem com criação de tabelas simples em CSV. O módulo não apenas gera as tabelas, mas também tem recursos para minimizar o seu preenchimento de dados. Também pode ser bem útil para alguns projetos que necessitem entregar tabelas que precisem ser trabalhadas em Office ou de integrar-se com algum banco de dados.

> Exemplo de leitura em SGBD e LibreOffice.
<div align="center"><img src="https://github.com/Vinicius-DevSys/GTables/blob/master/Referencias/Referencia%201.png" style="width:400px; height:175px;" alt="Descrição da imagem">
<img src="https://github.com/Vinicius-DevSys/GTables/blob/master/Referencias/Referencia%202.png" style="width:400px; height:175px;" alt="Descrição da imagem"></div>

## **Versão 1.0.0**
Nessa versão, entregamos o recurso citado na versão anterior, que torna possível minimizar o preenchimento de dados com a geração de dados fictícios, baseados na demanda do desenvolvedor. Também temos a entrega de um novo objeto chamado DataMaker; é ele que torna possível a geração de dados fictícios por meio de seus métodos. Nesta versão, houve a correção do erro com caracteres especiais, codificando as tabelas para UTF-8.

## Documentação
### TableMaker(columns)
Essa é a classe responsável pelo arquivo CSV que será gerado.

#### Parâmetros
- **columns** - Precisa receber uma lista para representar as colunas da sua tabela.
> A classe pede o parâmetro **columns** para evitar a criação de uma tabela sem colunas direto na criação do objeto já que lá mesmo elas ja estão sendo requisitadas.
> Dessa forma você pode adicionar as suas linhas separadamente sem se preocupar com quando/se já colocou a linha que representará as colunas.

#### Atributos
- **self.table** - Armazena toda a estrutura da tabela em uma lista.

#### Métodos
- **add_row(row):** Adiciona uma nova linha na tabela em **self.table**.
> row - Precisa receber uma lista para representar uma nova linha que será inserida na tabela **self.table**.
- **columns( ):** Retorna uma lista que contem os nomes de cada coluna.
- **check_table( ):** Retorna uma lista que contém todas as linhas da tabela CSV ou em outras palavras retorna a tabela inteira.
- **build( ):** Cria um arquivo com todo o conteúdo do atribulo self.table.

### DataMaker(substantive, adjective, last_number=0)
Essa é a classe responsável pela parte da geração de dados ficticios.

#### Parâmetros
- **substantive** - Adicione uma lista de substantivos (quanto maior a lista melhor) ou coisas que possam carregar o mesmo contexto para os seus objetivos.
- **adjective** - Adicione uma lista de adjetivos (quanto maior a lista melhor) ou coisas que possam carregar o mesmo contexto para os seus objetivos.
- **last_number** - Este parametro guarda apenas o último numero gerado como referência para gerar uma progressão numérica e você pode decidir em que valor ela se inicia, mas por padrão ele vem em 0.

#### Atributos
- **self.substantive** - Deve armazenar todos os substantivos em uma lista.
- **self.adjective** - Deve armazenar todos os adjetivos em uma lista.
- **self.last_number** - Deve armazenar o último numero gerado pelo objeto pra ser uma referência para o proximo número que for gerado. O valor atribuido na criação do objeto determina a refêrencia inicial da qual o número se inicia.

#### Métodos
- **create_name_data( )** - Esse método retorna uma string que é uma combinação aleatória da seguinte ordem: substantivo + adjetivo; sendo esses 2 elementos vindos das suas listas dos atributos **substantive** e **adjective**.
- **create_progress_data(minmax=[0, 10])** - Esse método gera um número que pra cada vez que seja chamado, gere um numero aleatoriamente maior que o ultimo, porém seguindo um alcanse que será determinado pelo atributo **minmax** que deve receber uma lista que determine o valor minimo e máximo a ser sorteado **Exemplo:** minmax=[18, 60].


## Teste
Esse é o arquivo de teste para a biblioteca.
> Experimente usar esse modelo para conhecer e testar a biblioteca.
```py
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
```
Perceba que não é obrigatório preencher todas as colunas para criar a sua tabela, assim como você também faria diretamente em um bloco de notas, mas terá futuramente a possibilidade de habilitar um limitador para manter a coerência entre linha e coluna.

## Dependências
- **csv** - Já vem com o seu Python, porém em algumas distros Linux pode haver alguma variação, fazendo-se necessário o download da dependência.
- **random** - Já vem com o seu Python, porém em algumas distros Linux pode haver alguma variação, fazendo-se necessário o download da dependência.

## Recomendações
- Use em projetos pequenos.
- Se a demanda logistica for altamente sofisticada talvez, seja melhor você optar por uma biblioteca que faça uso de banco de dados.

## Considerações
- **Documentação** - A documentação pode atualizar por commit, então, a cada nova versão podem haver mudanças significativas, assim como novas funcionalidades.
- **SOLID** - Esse módulo visa o alinhamento com o SOLID, as convenções do Python e de código limpo.
- **MVP** - Esse projeto segue a estrategia do MVP(Minimum Viable Product).
