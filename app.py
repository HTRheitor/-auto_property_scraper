from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import openpyxl
driver= webdriver.Chrome()
driver.get('https://www.imoveismartinelli.com.br/')

precos= driver.find_elements(By.XPATH, "//div[@class='card-valores']/div")
links= driver.find_elements(By.XPATH, "//a[@class='carousel-cell is-selected']")


workbook= openpyxl.load_workbook('imoveis.xlsx')
pagina_imoveis= workbook['precos']

for preco in zip(precos, links): 
    preco_formatado= preco.text.split(' ')[1]
    link_pronto= link.get_attribute('href')
    data_atual= datetime.now().strftime('%d/%m/%YS')
    pagina_imoveis.append([preco_formatado, link_pronto, data_atual])


workbook.save('imoveis.xlsx')

