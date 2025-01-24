"""
Esse programa realiza o preenchimento de um formulario basico
de um site para testes com selenium

# o site contém um erro no número de telefone
# o site não informa um formato especifico e 
# foram testados diversos formatos de data

# como é apenas um site para demonstração e testes
# não esta sendo realizado o envio do arquivo de imagem

# 1° - selenium não interaje diretamente com elementos 
# do sistema operacional

# 2° - isso me obrigaria a usar pyautogui para escrever 
# e confirmar o caminho 
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from time import sleep

opcoes = webdriver.ChromeOptions()
servico = Service(ChromeDriverManager().install())
opcoes.page_load_strategy = "normal" # esperar carregamento completo

navegador = webdriver.Chrome(opcoes, servico)
navegador.maximize_window()

# abrir site de demonstração de automação
site = 'https://demo.automationtesting.in/Register.html'
navegador.get(site)

# procurar primeiro nome
nome = navegador.find_element(By.CSS_SELECTOR, '#basicBootstrapForm > div:nth-child(1) > div:nth-child(2) > input')

# preencher nome
nome.send_keys("valter")

# procurar sobrenome
sobrenome = navegador.find_element(By.CSS_SELECTOR, '#basicBootstrapForm > div:nth-child(1) > div:nth-child(3) > input')

# preencher sobrenome
sobrenome.send_keys("Tertuliano")

# procurar endereço
endereco = navegador.find_element(By.CSS_SELECTOR, "#basicBootstrapForm > div:nth-child(2) > div > textarea")

# preencher endereço
endereco.send_keys("Rua Francisco Masini, 254, Jd Irene Santo André - SP")

# procurar email
email = navegador.find_element(By.CSS_SELECTOR, '#eid > input')

# Preencher email
email.send_keys('valtertert@gmail.com')

# procurar telefone
telefone = navegador.find_element(By.CSS_SELECTOR, '#basicBootstrapForm > div:nth-child(4) > div > input')

# preencher telefone
telefone.send_keys("+55 016 994030287")

# preencher genero
genero = navegador.find_element(By.CSS_SELECTOR, '#basicBootstrapForm > div:nth-child(5) > div > label:nth-child(1) > input').click()

# preencher passatempo
passatempo = navegador.find_element(By.CSS_SELECTOR, "#checkbox2").click()

# Procurar idioma

# - 1 abre o dropdown
caixa_pais = navegador.find_element(By.ID, "msdd")
caixa_pais.click()

# - 2 obtenha lista de opções
lista_paises = navegador.find_element(By.CLASS_NAME, 'ui-autocomplete')
navegador.implicitly_wait(3) # espera rapida para carregar lista

# - 3 marque o idioma
selecionar_idioma = lista_paises.find_element(By.CSS_SELECTOR, "#basicBootstrapForm > div:nth-child(7) > div > multi-select > div:nth-child(2) > ul > li:nth-child(35) > a")
selecionar_idioma.click()

# Procurar Habilidades

# - 1  opção com select - ID do select
obter_habilidades = navegador.find_element(By.ID,'Skills')

# iniciando a classe Select
habilidade = Select(obter_habilidades)

# selecionar categoria de habilidade
habilidade.select_by_value("Python")

# Procurar Pais
obter_pais = navegador.find_element(By.ID, "country")
navegador.implicitly_wait(1)
escolher_pais = Select(obter_pais)
navegador.implicitly_wait(1)
escolher_pais.select_by_index(9)

# Procurar ano
obter_ano = navegador.find_element(By.ID, 'yearbox')
escolher_ano = Select(obter_ano)
escolher_ano.select_by_value('1994')

# Procurar Mês
obter_mes = navegador.find_element(By.CSS_SELECTOR, "#basicBootstrapForm > div:nth-child(11) > div:nth-child(3) > select")
escolher_mes = Select(obter_mes)
escolher_mes.select_by_value("October")

# Procurar dia
obter_dia = navegador.find_element(By.ID, 'daybox')
escolher_dia = Select(obter_dia)
escolher_dia.select_by_value("13")

# Nova senha
senha = "123456789"
nova_senha = navegador.find_element(By.ID, 'firstpassword')
nova_senha.send_keys(senha)

#confirmar senha
confirmar_senha = navegador.find_element(By.ID, 'secondpassword')
confirmar_senha.send_keys(senha)

# enviar formulario
enviar = navegador.find_element(By.ID, 'submitbtn').click()
sleep(10)
navegador.quit()