from classes import *
import os
tasks = ToDoList()

def menu():
    a = 1
    while a == 1:
        try:
            print ("---To do list---")
            print("Escolha o que deseja fazer:")
            print(" ")
            print("[1] Adicionar tarefa")
            print("[2] Excluir tarefa")
            print("[3] Listar tarefas")
            print("[4] Sair")
            menu = int (input("-> "))
            match menu:
                case 1:
                    os.system("cls")
                    descrição = input("Escreva uma tarefa para adicionar: ")
                    tasks.adicionar_tarefa(descrição)
                    os.system("pause")
                case 2:
                    os.system("cls")
                    excluir = input("Qual tarefa deseja excluir?: ")
                    tasks.excluir_tarefa(excluir)
                    os.system("pause")
                case 3:
                    os.system("cls")
                    print("Essa é a lista de suas tarefas: ")
                    tasks.listar_tarefas()
                    os.system("pause")
                case 4:
                    a = 0
                case _:
                    os.system("cls")
                    print("opção inválida")
                    os.system("pause")

        except Exception as erro:
            print("Opção inválida")


