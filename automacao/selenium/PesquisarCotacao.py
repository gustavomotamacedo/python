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

tabela.to_excel(r'C:\Users\Gustavo Macedo\Documents\GitHub\python\automacao\selenium\Produtos_Velho.xlsx', index = False)

#atualiza a coluna 'cortação'
for i in range(len(tabela['Moeda'])):
        if tabela['Moeda'][i] == 'Dólar':
            #dolar
            tabela['Cotação'][i] = dolar
        elif tabela['Moeda'][i] == 'Euro':
            #euro
            tabela['Cotação'][i] = euro
        else:
            #ouro
            tabela['Cotação'][i] = ouro

# atualizando preços
for i in range(len(tabela['Preço de Compra'])):
    #preço de compra
    tabela['Preço de Compra'][i] = float(tabela['Preço Original'][i]) * float(tabela['Cotação'][i])

for i in range(len(tabela['Preço de Venda'])):
    #preço de venda
    tabela['Preço de Venda'][i] = float(tabela['Preço de Compra'][i]) * float(tabela['Margem'][i])

#criando uma nova tabela, atualizada
tabela.to_excel(r'C:\Users\Gustavo Macedo\Documents\GitHub\python\automacao\selenium\Produtos_Novo.xlsx', index= False) #index é false para não salvar a coluna automática index!
