import time
from pesquisas import Pesquisa

class Gerador:
    def __init__(self, dados, formato="txt"):
        self.dados = dados
        if(formato == "txt" or formato == ".txt" ):
            self.__geraTxt()

            
    def __geraTxt(self):
        self.__arrumaDados()
        print(self.dados)
        campos = list(self.dados.keys())
        with open("log.txt", "w") as file:
            for linha in range(len(self.dados["Dia da semana"])):
                for coluna in range(len(campos)):
                    for dado in str(self.dados[campos[coluna]][linha]):
                        file.write(dado)
                    file.write("\n")
                file.write("\n")

    def __arrumaDados(self):
        diaAnt = 0
        flag = 0
        novoDia = list()
        campos = list(self.dados.keys())
        for dia in range(len(self.dados["Dia da semana"])):
            if self.dados["Dia da semana"][dia] != diaAnt:
                novoDia.append(self.dados["Dia da semana"][dia])
                for campo in range(len(campos)):
                    if campo != 0:
                        var = list()
                        var.append(self.dados[campos[campo]][dia])
                        self.dados[campos[campo]][dia-flag] = list()
                        self.dados[campos[campo]][dia-flag].append(var[0])
            else:
                flag+=1
                for campo in range(len(campos)):
                    if campo != 0:
                        self.dados[campos[campo]][diaAnt-2].append(self.dados[campos[campo]][dia])
            diaAnt = self.dados["Dia da semana"][dia]
        self.dados["Dia da semana"] = novoDia
        pos = 1
        while(True):
            if type(self.dados[campos[pos]][-1])!=list:
                self.dados[campos[pos]].pop(-1)
            else:
                pos += 1
            if pos>=len(campos):
                break
            
if __name__ == "__main__":
    login = open("saveLogin.txt", "r")
    dados = login.read().split(",")
    matricula = dados[0]
    senha = dados[1]

    pesquisa = Pesquisa(matricula, senha)
    dados = pesquisa.pegaDados()
    log = Gerador(dados)
