import fila

teste_evasao = fila.Sistema()
teste_evasao.cadastrar_ficha("10")
teste_evasao.chamar_proxima_ficha()
teste_evasao.visualizar_pacientes_aguardando()
teste_evasao.chamar_proxima_ficha()
teste_evasao.chamar_proxima_ficha()
teste_evasao.visualizar_pacientes_aguardando()
teste_evasao.rechamar_ficha("10")
teste_evasao.consultar_estado("10")
teste_evasao.registrar_evasao("10")
teste_evasao.consultar_estado("10")