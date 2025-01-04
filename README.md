# GTables 0.9.0 - Gerador-de-Tabelas-CSV
> ### <img src="https://github.com/Vinicius-DevSys/GTables/blob/master/Referencias/python.png" width="55" alt="Descrição da imagem"> Conteúdo: Python, CSV, LibreOffice, SGBD, SOLID.

Esse é um módulo para te auxiliar a criar tabelas simples em CSV para você usar no seu banco de dados, LibreOffice ou onde mais você desejar.

## Descrição
Esse módulo serve para você implementar códigos que trabalhem com criação de tabelas simples em CSV. O módulo não apenas gera as tabelas, mas também tem recursos para minimizar o seu preenchimento de dados. Também pode ser bem útil para alguns projetos que necessitem entregar tabelas que precisem ser trabalhadas em Office ou de integrar-se com algum banco de dados.

> Exemplo de leitura em SGBD e LibreOffice.
<div align="center"><img src="https://github.com/Vinicius-DevSys/GTables/blob/master/Referencias/Referencia%201.png" style="width:400px; height:175px;" alt="Descrição da imagem">
<img src="https://github.com/Vinicius-DevSys/GTables/blob/master/Referencias/Referencia%202.png" style="width:400px; height:175px;" alt="Descrição da imagem"></div>

## **Versão 0.9.0**
Essa é a primeira versão e atende apenas a um dos objetivos principais: gerar tabelas. Quando for possível minimizar preenchimento de dados chegaremos a versão 1.0.0.

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

## Teste
Esse é o arquivo de teste para a biblioteca.
> Experimente usar esse modelo para conhecer e testar a biblioteca.
```py
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
```
Perceba que não é obrigatório preencher todas as colunas para criar a sua tabela, assim como você também faria diretamente em um bloco de notas, mas terá futuramente a possibilidade de habilitar um limitador para manter a coerência entre linha e coluna.

## Dependências
- **csv** - Já vem com o seu Python, porém em algumas distros Linux pode haver alguma variação, fazendo-se necessário o download da dependência.

## Recomendações
- Use em projetos pequenos.
- Se a demanda logistica for altamente sofisticada talvez, seja melhor você optar por uma biblioteca que faça uso de banco de dados.

## Considerações
- **Documentação** - A documentação pode atualizar por commit, então, a cada nova versão podem haver mudanças significativas, assim como novas funcionalidades.
- **SOLID** - Esse módulo visa o alinhamento com o SOLID, as convenções do Python e de código limpo.
- **MVP** - Esse projeto segue a estrategia do MVP(Minimum Viable Product).
