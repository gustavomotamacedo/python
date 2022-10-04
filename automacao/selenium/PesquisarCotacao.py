from selenium import webdriver # controlar o navegador
from selenium.webdriver.common.keys import Keys # usar o teclado
from selenium.webdriver.common.by import By # localizar os itens do navegador
import pandas as pd # pandas é uma biblioteca para mexer com base de dados
# IMPORT'S PADRÃO DO SELENIUM

navegador = webdriver.Chrome()

# abrindo o google
navegador.get('https://www.google.com/')

#pegando uma cotação (dolar)

# #parametro e codigo do parametro
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dolar')
#localiza o input de busca do google e escreve 'cotação dolar'

#clica enter para pesquisar
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

# dolar recebe o valor da cotação do dolar
dolar = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text

navegador.get('https://www.google.com/')
# #parametro e codigo do parametro
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro', Keys.ENTER)
#localiza o input de busca do google e escreve 'cotação euro' e da enter

euro = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text

navegador.get('https://www.melhorcambio.com/ouro-hoje')

ouro = navegador.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute('value')

navegador.quit()

dolar = dolar.replace(',', '.')
euro = euro.replace(',', '.')
ouro = ouro.replace(',', '.')

#coloacando os dados na base de dados

tabela = pd.read_excel(r'C:\Users\Gustavo Macedo\Documents\GitHub\python\automacao\selenium\Produtos.xlsx')

print(tabela)

i = 0

#atualiza a coluna 'cortação'

for tipo in tabela['Moeda']:
    if tipo == 'Dólar':
        tabela['Cotação'][i] = dolar
    elif tipo == 'Euro':
        tabela['Cotação'][i] = euro
    else:
        tabela['Cotação'][i] = ouro
    i += 1

print(tabela)

# atualizando preços
i = 0

for preco in tabela['Preço de Compra']:
    tabela['Preço de Compra'][i] = float(tabela['Preço Original'][i]) * float(tabela['Cotação'][i])
    i += 1

print(tabela)

i = 0

for preco in tabela['Preço de Venda']:
    tabela['Preço de Venda'][i] = float(tabela['Preço de Compra'][i]) * float(tabela['Margem'][i])
    i += 1

print(tabela)

#criando uma nova tabela, atualizada
tabela.to_excel(r'C:\Users\Gustavo Macedo\Documents\GitHub\python\automacao\selenium\Produtos_Novo.xls', index= False) #index é false para não salvar a coluna automática index!
