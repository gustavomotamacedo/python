from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

navegador = webdriver.Chrome()

navegador.get('https://www.google.com/')

navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dolar')

navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

dolar = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text

navegador.get('https://www.google.com/')

navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro', Keys.ENTER)

euro = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text

navegador.get('https://www.melhorcambio.com/ouro-hoje')

ouro = navegador.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute('value')

navegador.quit()

dolar = dolar.replace(',', '.')
euro = euro.replace(',', '.')
ouro = ouro.replace(',', '.')

tabela = pd.read_excel(r'C:\Users\Gustavo Macedo\Documents\GitHub\python\automacao\selenium\Produtos.xlsx')

tabela.to_excel(r'C:\Users\Gustavo Macedo\Documents\GitHub\python\automacao\selenium\Produtos_Velho.xlsx', index = False)

tabela.loc[tabela['Moeda'] == 'Dólar', 'Cotação'] = float(dolar)
tabela.loc[tabela['Moeda'] == 'Euro', 'Cotação'] = float(euro)
tabela.loc[tabela['Moeda'] == 'Ouro', 'Cotação'] = float(ouro)

tabela['Preço de Compra'] = tabela['Preço Original'] * tabela['Cotação']

tabela['Preço de Venda'] = tabela['Preço de Compra'] * tabela['Margem']

tabela.to_excel(r'C:\Users\Gustavo Macedo\Documents\GitHub\python\automacao\selenium\Produtos_Novo.xlsx', index= False)
