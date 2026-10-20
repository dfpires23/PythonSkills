import logging

# ======== MANIPULAÇÃO DE ARQUIVOS =======
# r - read (ler o conteúdo do arquivo, default)
# a - append (adiciona ao final do arquivo, sem apagar o conteúdo existente)
# a+ - append + read (adiciona ao final do arquivo, e permite ler o conteúdo do arquivo)
# x - create (cria o arquivo, mas se ele já existe, gera um erro)
# w - write (apaga o conteúdo existente e escreve o novo conteúdo)
# w+ - write + read (apaga o conteúdo existente, escreve o novo conteúdo, e permite ler o conteúdo do arquivo)

# ===================================================================================================================
## ABRE O ARQUIVO PARA ESCRITA E ESCREVE NO ARQUIVO
file = open("pasta_exemplo/exemplo.txt", "a")
file.write("Linha 1\n")
file.write("Nome: Daniel\n")
file.close()  # FECHA O ARQUIVO

# SE NÃO FECHAR O ARQUIVO, CRIA UM MEMORY LEAK, POIS O ARQUIVO FICA ABERTO PARA SEMPRE, E NÃO PODE SER ACESSADO POR OUTROS PROGRAMAS
# PARA EVITAR ISSO, É MELHOR USAR O WITH, QUE GARANTE QUE O ARQUIVO SEJA FECHADO CORRETAMENTE, MESMO QUE OCORRA UM ERRO
## with open("exemplo.txt", "a") as file:

## ABRE O ARQUIVO PARA LEITURA E IMPRIME O CONTEÚDO NA TELA
file = open("pasta_exemplo/exemplo.txt", "r")
print(file.read())

file.seek(0)  # VOLTA O CURSOR PARA O INÍCIO DO ARQUIVO

# LÊ O CONTEÚDO DO ARQUIVO E RETORNA UMA LISTA DE LINHAS
array_linhas = file.readlines()
print(array_linhas)

file.close()  # FECHA O ARQUIVO
# ===================================================================================================================

# === EXERCÍCIO ===
file = open("pasta_exemplo/orçamento.csv", "r")
texto = file.read()
file.close()

file = open("pasta_exemplo/orçamento_ponto_virgula.csv", "w")
novo_texto = texto.replace(",", ";")  # SUBSTITUI TODAS AS VÍRGULAS POR PONTOS E VÍRGULAS, E RETORNA O NOVO TEXTO
file.write(novo_texto)
file.close()

### == USO DE WITH ==================================================================================================
with open("pasta_exemplo/exemplo.txt", "a+") as file:
    file.write("Linha 2\n")
    file.write("Idade: 30\n")

    file.seek(0)
    print(file.read())  # LÊ O CONTEÚDO DO ARQUIVO
    print(texto)
### ===================================================================================================================

# =====
# TRY...EXCEPT, PARA TRATAR ERROS SEM SAIR DO PROGRAMA
try:
    with open("pasta_exemplo/exemplo.txt", "x") as file:
        file.write("Linha 1\n")
        file.write("Nome: Daniel\n")
except FileExistsError as e:
    print(type(e))  # IMPRIME O TIPO DO ERRO
    print(type(e).__name__)  # IMPRIME O NOME DO ERRO

    print(e)  # IMPRIME A MENSAGEM DE ERRO

    print(type(e).__name__, "->", str(e))  # IMPRIME O NOME DO ERRO E A MENSAGEM DE ERRO, USANDO VÍRGULA PARA SEPARAR OS ARGUMENTOS, O QUE ADICIONA UM ESPAÇO ENTRE OS ARGUMENTOS
    print(type(e).__name__ + "->" + str(e))  # IMPRIME O NOME DO ERRO E A MENSAGEM DE ERRO, USANDO CONCATENAÇÃO DE STRINGS

except Exception as e:
    raise e  # RE-LEVANTA O ERRO, PARA QUE ELE SEJA EXIBIDO NA TELA, E O PROGRAMA SEJA INTERROMPIDO, POIS O ERRO NÃO FOI TRATADO ESPECIFICAMENTE

print("Programa continua...\n")  # ESTE CÓDIGO SERÁ EXECUTADO APESAR DO ERRO, POIS O ERRO FOI TRATADO PELO EXCEPT, E O PROGRAMA NÃO FOI INTERROMPIDO PELO ERRO

### ===================================================================================================================
## USO DO MÓDULO DE LOGGING PARA REGISTRAR ERROS EM UM ARQUIVO DE LOG, AO INVÉS DE EXIBIR O ERRO NA TELA, O QUE PERMITE QUE O PROGRAMA CONTINUE EXECUTANDO MESMO QUE OCORRA UM ERRO, E PERMITE ANALISAR OS ERROS POSTERIORMENTE NO ARQUIVO DE LOG

logger = logging.getLogger(__name__)  # CRIA UM OBJETO LOGGER, QUE É USADO PARA REGISTRAR MENSAGENS DE LOG
logging.basicConfig(filename="app.log", level=logging.INFO)  # CONFIGURA O MÓDULO DE LOGGING PARA REGISTRAR MENSAGENS DE LOG NO ARQUIVO "app.log", COM O NÍVEL DE LOGGING INFO (INFORMAÇÕES, AVISOS, ERROS, ETC)

try:
    with open("pasta_exemplo/orçamento_dummy.csv", "r") as file:
        print(file.read())
except Exception:
    logger.exception("Erro ao ler o arquivo orçamento_dummy.csv")  # REGISTRA A MENSAGEM DE LOG DE ERRO, INCLUINDO A PILHA DE ERROS (STACK TRACE)
    # raise  # NÃO RE-LEVANTA O ERRO, APENAS REGISTRA O ERRO NO ARQUIVO DE LOG, E CONTINUA A EXECUÇÃO DO PROGRAMA

## ===================================================================================================================

try:
    with open("pasta_exemplo/orçamento_dummy.csv", "r") as file:
        print(file.read())
except Exception:
    logger.exception("Erro ao ler o arquivo orçamento_dummy.csv")  # REGISTRA A MENSAGEM DE LOG DE ERRO, INCLUINDO A PILHA DE ERROS (STACK TRACE)
    raise  # RE-LEVANTA O ERRO, PARA QUE ELE SEJA EXIBIDO NA TELA, E O PROGRAMA SEJA INTERROMPIDO, POIS O ERRO NÃO FOI TRATADO ESPECIFICAMENTE
