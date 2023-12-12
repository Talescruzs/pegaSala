from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pesquisas import Pesquisa


if __name__ == "__main__":
    login = open("saveLogin.txt", "r")
    dados = login.read().split(",")
    matricula = dados[0]
    senha = dados[1]

    pesquisa = Pesquisa(matricula, senha)
    print(pesquisa.pegaDados())
