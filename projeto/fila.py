# Constantes
STATUS_AGUARDANDO = "aguardando"
STATUS_CHAMADO = "chamado"
STATUS_ATENDIDO = "atendido"
STATUS_EVASAO = "evasao"

class Sistema:
    def __init__(self):
        self.fichas = {}
        self.ultimo_chamado = None

    def  cadastrar_ficha_simulada(self, numero_ficha):
        if numero_ficha in self.fichas:
            print(f"Ficha {numero_ficha} já está cadastrada.")
            return False
        self.fichas[numero_ficha] = {"status": STATUS_AGUARDANDO}
        return True

    def chamar_proxima_ficha(self):
        for numero_ficha, ficha in self.fichas.items():
            if ficha["status"] == STATUS_AGUARDANDO:
                ficha["status"] = STATUS_CHAMADO
                self.ultimo_chamado = numero_ficha
                return numero_ficha
        return None

    def rechamar_ficha(self, numero_ficha):
        if numero_ficha in self.fichas and self.fichas[numero_ficha]["status"] == STATUS_CHAMADO:
            print(f"Ficha {numero_ficha} foi rechamada.")
            return True
        return False

    def registrar_atendimento(self, numero_ficha):
        if numero_ficha in self.fichas and self.fichas[numero_ficha]["status"] == STATUS_CHAMADO:
            self.fichas[numero_ficha]["status"] = STATUS_ATENDIDO
            return True
        return False
    
    def registrar_evasao(self, numero_ficha):
        if numero_ficha in self.fichas and self.fichas[numero_ficha]["status"] == STATUS_CHAMADO:
            self.fichas[numero_ficha]["status"] = STATUS_EVASAO
            return True
        return False

    def visualizar_pacientes_aguardando(self):
        aguardando = []
        for numero_ficha, ficha in self.fichas.items():
            if ficha["status"] == STATUS_AGUARDANDO:
                print(f"Ficha {numero_ficha}: Aguardando")
                aguardando.append(numero_ficha)
        if not aguardando:
            print("Não há pacientes aguardando.")

    def consultar_posicao(self, numero_ficha):
        if numero_ficha not in self.fichas:
            print(f"Ficha {numero_ficha} não encontrada.")
            return None
        ficha_consultada = self.fichas[numero_ficha]
        if ficha_consultada["status"] != STATUS_AGUARDANDO:
            print(f"Ficha {numero_ficha}: Status atual é '{ficha_consultada['status']}'. Não está na fila.")
            return 0
        posicao = 0
        for ficha_numero, ficha in self.fichas.items():
            if ficha["status"] == STATUS_AGUARDANDO:
                posicao += 1
            if ficha_numero == numero_ficha:
                break
        print(f"Ficha {numero_ficha}: Aguardando (Posição na fila: {posicao})")
        return posicao

    def consultar_estado(self, numero_ficha):
        if numero_ficha in self.fichas:
            status = self.fichas[numero_ficha]["status"]
            print(f"Ficha {numero_ficha}: Status - {status}")
            return status
        else:
            print(f"Ficha {numero_ficha} não encontrada.")