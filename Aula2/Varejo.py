import pandas as pd
import plotly.express as px


# Importação banco de dados
tabela = pd.read_csv(r"C:\Users\Administrador\Downloads\Aula2\clientes.csv", encoding="latin", sep=";")

# Tratamento de dados, exclusao de coluna e visualização de dados vazio
tabela = tabela.drop("Unnamed: 8", axis=1)  # exclusao da coluna
# print(tabela.info()) #visualiza as info da tabela
tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"],
                                             errors="coerce")  # coerce força a virar numero
tabela = tabela.dropna()  # excluindo dados vazios no BD
# print(tabela.info())

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, y="Nota (1-100)", histfunc="avg", text_auto=True)
    grafico.show()

#Perfil Ideal
