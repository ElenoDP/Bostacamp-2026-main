import tkinter as tk
from fila import Sistema
from tkinter import messagebox

sistema = Sistema()

class Janela:
    def __init__(self):
        self.janela = tk.Tk()
        self.sistema = sistema 
        self.janela.title("Recepção - Ambulatório AME UNIMAR")

        self.titulo = tk.Label(self.janela, text="AMBULATÓRIO UNIMAR", font=("Arial", 30))
        self.titulo.pack()

        self.ultima_chamada = tk.Label(self.janela, text=f"Último paciente chamado: ainda não houve chamadas")
        self.ultima_chamada.pack(pady=20)

        self.fila_espera = tk.Label(self.janela, text="Fila de espera:")
        self.fila_espera.pack(pady=10)
        self.atualizar_nomes_espera()

        tk.Label(self.janela, text="Digite o nome do paciente:").pack(pady=10)
        self.entrada_nome = tk.Entry(self.janela)
        self.entrada_nome.pack(pady=10)

        self.cadastrar = tk.Button(self.janela, text="Cadastrar paciente", command=self.cadastrar_nome)
        self.cadastrar.pack(pady=10)

        self.chamar_proxima = tk.Button(self.janela, text="Chamar Próximo paciente", command=self.chamar_proximo_nome)
        self.chamar_proxima.pack(pady=20)

        self.rechamar = tk.Button(self.janela, text="Rechamar paciente", command=self.rechamar_ficha)
        self.rechamar.pack(pady=20)

        self.registrar_evasao = tk.Button(self.janela, text="Registrar Evasão", command=self.registrar_evasao)
        self.registrar_evasao.pack(pady=20)

        tk.Button(self.janela, text="Abrir Visor do Paciente", command=self.abrir_visor_paciente).pack()

    def iniciar(self):
        self.janela.mainloop()

    def cadastrar_nome(self):
        nome = self.entrada_nome.get()
        if self.sistema.cadastrar_ficha_simulada(nome):
            messagebox.showinfo("Informação", f"Paciente {nome} cadastrado com sucesso.")
        else:
            messagebox.showwarning("Aviso", f"Paciente {nome} já está cadastrado.")
        
        self.atualizar_nomes_espera()

    def atualizar_nomes_espera(self):
        self.fila_espera.config(
            text="Fila de espera: " + ", ".join(
                [
                    f"Paciente {numero}"
                    for numero, ficha in self.sistema.pacientes.items()
                    if ficha["status"] == "aguardando"
                ]
            )
        )
    def chamar_proximo_nome(self):
        nome = self.sistema.chamar_proxima_ficha()

        if nome:
            self.ultima_chamada.config(text=f"Último paciente chamado: {nome}")
            self.atualizar_nomes_espera()
            messagebox.showinfo("Informação", f"Paciente {nome} chamado para atendimento.")
        else:
            messagebox.showinfo("Informação", "Não há ninguém aguardando atendimento.")

    def rechamar_ficha(self):
        nome = self.sistema.ultimo_chamado

        if nome:
            if self.sistema.rechamar_ficha(nome):
                messagebox.showinfo("Informação", f"Paciente {nome} foi rechamado.")
            else:
                messagebox.showwarning("Aviso", f"Paciente {nome} não pode ser rechamado.")
        else:
            messagebox.showinfo("Informação", "Não há ficha para rechamar.")

    def registrar_evasao(self):
        nome = self.sistema.ultimo_chamado

        if nome:
            if self.sistema.registrar_evasao(nome):
                messagebox.showinfo("Informação", f"Paciente {nome} registrada como evadida.")
            else:
                messagebox.showwarning("Aviso", f"Paciente {nome} não pode ser registrada como evadida.")
        else:
            messagebox.showinfo("Informação", "Não há paciente para registrar evasão.")
            
    def abrir_visor_paciente(self):
        JanelaPaciente()

class JanelaPaciente:
    def __init__(self):
        self.janela = tk.Toplevel()
        self.sistema = sistema
        self.janela.title("Paciente visor")

        self.titulo = tk.Label(self.janela, text="AMBULATÓRIO UNIMAR", font=("Arial", 30))
        self.titulo.pack()

        tk.Label(self.janela, text="Digite o nome do paciente:").pack(pady=10)
        self.entrada_nome = tk.Entry(self.janela)
        self.entrada_nome.pack(pady=10)

        self.consultar_todos_dados = tk.Button(self.janela, text="Consultar dados", command=self.consultar_dados)
        self.consultar_todos_dados.pack(pady=20)

    def consultar_dados(self):
        numero = self.entrada_nome.get()
        posicao = self.sistema.consultar_posicao(numero)

        numero = self.entrada_nome.get()
        estado = self.sistema.consultar_estado(numero)

        if posicao is not None and estado is not None:
            if posicao == 0:
                messagebox.showinfo("Informação", f"Paciente {numero}: Estado - {estado}\n\n\n Você é o próximo a ser atendido!")
            elif posicao > 0 and posicao < 3:
                messagebox.showinfo("Informação", f"Paciente {numero}: Posição na fila - {posicao}, Estado - {estado}\n\n\n Aguarde, seu atendimento está se aproximando.")
            elif posicao > 3 and posicao < 6:
                messagebox.showinfo("Informação", f"Paciente {numero}: Posição na fila - {posicao}, Estado - {estado}\n\n\n Há poucos pacientes a frente!")
            else:
                messagebox.showinfo("Informação", f"Paciente {numero}: Posição na fila - {posicao}, Estado - {estado}\n\n\n Há muitos pacientes a frente.")
        else:
            messagebox.showinfo("Informação", f"Paciente {numero} não está na fila.")