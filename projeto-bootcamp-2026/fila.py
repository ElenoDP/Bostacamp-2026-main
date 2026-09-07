# Constantes
STATUS_AGUARDANDO = "aguardando"
STATUS_CHAMADO = "chamado"
STATUS_ATENDIDO = "atendido"
STATUS_EVASAO = "evasao"

class Sistema:
    def __init__(self):
        self.pacientes = {}
        self.ultimo_chamado = None

    def  cadastrar_paciente(self, nome_paciente):
        if nome_paciente in self.pacientes:
            print(f"Paciente {nome_paciente} já está cadastrado.")
            return False
        self.pacientes[nome_paciente] = {"status": STATUS_AGUARDANDO}
        return True

    def chamar_proximo_paciente(self):
        for nome_paciente, ficha in self.pacientes.items():
            if ficha["status"] == STATUS_AGUARDANDO:
                ficha["status"] = STATUS_CHAMADO
                self.ultimo_chamado = nome_paciente
                return nome_paciente
        return None

    def rechamar_paciente(self, nome_paciente):
        if nome_paciente in self.pacientes and self.pacientes[nome_paciente]["status"] == STATUS_CHAMADO:
            print(f"Paciente {nome_paciente} foi rechamado.")
            return True
        return False

    def registrar_atendimento(self, nome_paciente):
        if nome_paciente in self.pacientes and self.pacientes[nome_paciente]["status"] == STATUS_CHAMADO:
            self.pacientes[nome_paciente]["status"] = STATUS_ATENDIDO
            return True
        return False

    def registrar_evasao(self, nome_paciente):
        if nome_paciente in self.pacientes and self.pacientes[nome_paciente]["status"] == STATUS_CHAMADO:
            self.pacientes[nome_paciente]["status"] = STATUS_EVASAO
            return True
        return False

    def visualizar_pacientes_aguardando(self):
        aguardando = []
        for nome_paciente, ficha in self.pacientes.items():
            if ficha["status"] == STATUS_AGUARDANDO:
                print(f"Paciente {nome_paciente}: Aguardando")
                aguardando.append(nome_paciente)
        if not aguardando:
            print("Não há pacientes aguardando.")

    def consultar_posicao(self, nome):
        if nome not in self.pacientes:
            print(f"Paciente {nome} não encontrado.")
            return None

        paciente_consultado = self.pacientes[nome]

        if paciente_consultado["status"] != STATUS_AGUARDANDO:
            print(f"Paciente {nome} não está aguardando.")
            return 0

        pessoas_a_frente = 0
        for nome_paciente, paciente in self.pacientes.items():
            if nome_paciente == nome:
                break

            if paciente["status"] == STATUS_AGUARDANDO:
                pessoas_a_frente += 1

        return pessoas_a_frente

    def consultar_estado(self, nome_paciente):
        if nome_paciente in self.pacientes:
            status = self.pacientes[nome_paciente]["status"]
            print(f"Paciente {nome_paciente}: Status - {status}")
            return status
        else:
            print(f"Paciente {nome_paciente} não encontrado.")