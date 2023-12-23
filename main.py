from tkinter import *
from tkinter import ttk
from view import *
from pesquisas import Pesquisa

if __name__ == "__main__":
    user = getLogin()
    root = Tk()
    if not(user):
        login(root)
        user = getLogin()

    matricula = user[0]
    senha = user[1]
    pesquisa = Pesquisa(matricula, senha)

    print(pesquisa.pegaDados())

    root.mainloop()