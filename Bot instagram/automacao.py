# Instalação do selenium
import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

servico = Service(GeckoDriverManager().install())

navegador = webdriver.Firefox(service=servico)

# Entrar no instagram
navegador.get("https://www.instagram.com")
time.sleep(2)
# Fazer login

navegador.find_element(
    By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input').send_keys("Seu_login")
navegador.find_element(
    By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input').send_keys("Sua_senha")
navegador.find_element(
    By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div').click()
time.sleep(5)

# Clicar em não salvar informações
navegador.find_element(
    By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
time.sleep(1)

# Pesquisar
navegador.find_element(
    By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div").click()
navegador.find_element(
    By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input').send_keys("Perfil_para_seguir")
time.sleep(1)
navegador.find_element(
    By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/a/div/div/div/div[2]/div/div/div/span').click()
time.sleep(3)
# Seguir
navegador.find_element(
    By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/div/div[1]/button").click()
