from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
navegador.get("https://demo.automationtesting.in/WebTable.html")
sleep(5)

# obter dados da tabela
localizar_tags = navegador.find_elements(By.TAG_NAME,  'div')

for tag in localizar_tags:
    if tag.text == 'First Name':
        print('Ordenando as linhas da tabela pela coluna do primeiro nome: ')
        print("Em ordem crescente") 
        tag.click()

sleep(5)
navegador.quit()