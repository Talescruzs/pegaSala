from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Pesquisa:
    def __init__(self, matricula, senha):
        self.matricula = matricula
        self.senha = senha
        self.__login()
        self.driver.get("https://portal.ufsm.br/estudantil/relatorio/quadroHorariosAluno/form.html")
        self.driver.find_element(By.XPATH, '//*[@id="gerar"]').click()
        self.__geraDados()
        self.__geraSala()
        self.__close()

    def __login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://portal.ufsm.br/estudantil/index.html")

        self.driver.find_element(By.ID, "login").send_keys(self.matricula)
        self.driver.find_element(By.ID, "senha").send_keys(self.senha)
        self.driver.find_element(By.XPATH, "//*[@id='tab0']/form/div[4]/div/button").click()
    
    def __geraDados(self):
        dados = dict()
        colunas = self.driver.find_elements(By.XPATH, '//*[@id="quadro"]/thead/tr/th')
        linhas = self.driver.find_elements(By.XPATH, '//*[@id="quadro"]/tbody/tr')
        for a in range(len(colunas)):
            itens = list()
            for b in range(len(linhas)):
                itens.append(self.driver.find_element(By.XPATH, '//*[@id="quadro"]/tbody/tr[{0}]/td[{1}]'.format(b+1, a+1)).text)
            dados[self.driver.find_element(By.XPATH, '//*[@id="quadro"]/thead/tr/th[{0}]'.format(a+1)).text] = itens
        self.dados = dados

    def __geraSala(self):
        salas = list()
        ids = self.dados["Código"]
        dias = self.dados["Dia da semana"]
        for dia in range(len(dias)):
            if dias[dia] == "Segunda-feira":
                dias[dia] = 2
            if dias[dia] == "Terça-feira":
                dias[dia] = 3
            if dias[dia] == "Quarta-feira":
                dias[dia] = 4
            if dias[dia] == "Quinta-feira":
                dias[dia] = 5
            if dias[dia] == "Sexta-feira":
                dias[dia] = 6

        self.driver.get("https://oca.ctism.ufsm.br/ensalamento/consulta-tabela.html")
        for a in range(len(ids)):
            self.driver.find_element(By.XPATH, '//*[@id="aulas1"]').clear()
            self.driver.find_element(By.XPATH, '//*[@id="aulas1"]').send_keys(ids[a])
            time.sleep(2)
            self.driver.find_element(By.XPATH, '/html/body/div[1]/button[{0}]'.format(dias[a])).click()
            time.sleep(2)
            salas.append(self.driver.find_element(By.XPATH, '//*[@id="dados-tabela"]/tr[not(@style) or @style!="display: none;"]/td[5]').text)
        self.dados["Salas"] = salas
    
    def pegaDados(self):
        return self.dados

    def __close(self):
        self.driver.close()

if __name__ == "__main__":
    login = open("saveLogin.txt", "r")
    dados = login.read().split(",")
    matricula = dados[0]
    senha = dados[1]


    pesquisa = Pesquisa(matricula, senha)
    print(pesquisa.pegaDados())