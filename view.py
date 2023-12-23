from tkinter import *
from tkinter import ttk

def saveLogin(matricula, senha):
    f = open("saveLogin.txt", "w")
    f.write("{0},{1}".format(matricula,senha))
    f.close()

def getLogin():
    data = False
    try:
        f = open("saveLogin.txt", "r")
        data = f.read().split(",")
        f.close()
    except:
        pass
    return data

def login(root):

    root.title("Pega Sala")
    h1 = Label(root, text="Insira seus dados para pesquisar as salas")

    nameMatricula = Label(root, text="Matricula")
    nameSenha = Label(root, text="Senha")

    matricula = Entry(root, width=100)
    senha = Entry(root, width=100)
    botao = Button(root, text="Rodar código", command=lambda: saveLogin(matricula.get(), senha.get()))

    h1.grid(column=1, row=0)
    nameMatricula.grid(column=0, row=1)
    matricula.grid(column=1, row=1)
    nameSenha.grid(column=0, row=2)
    senha.grid(column=1, row=2)
    botao.grid(column=1, row=3)



if __name__ == "__main__":
    root = Tk()
    if not(getLogin()):
        login(root)
    else:
        pass
    root.mainloop()