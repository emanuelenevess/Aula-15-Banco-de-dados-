import mysql.connector
from mysql.connector import Error

def conectar(): #TENTA SE CONECTAR AO BANCO DE DADOS
    try:
        conexao = mysql.connector.connect(
        host="localhost", #ENDEREÇO LOCAL (NÃO É NA NUVEM)
        user="root", #USUÁRIO
        password="senai", #SENHA
        database="estodolist" #DATABASE CRIADO ANTERIORMENTE
        )

        cursor = conexao.cursor(dictionary=True) #SE DER CERTO ELE CRIA UM CURSOR 
        #RETORNA DUAS INFORMAÇÕES:CONVEXÃO E CURSOR 
        return conexao,cursor
    except Error as erro:
        print(f"ERRO! Falha ao se conectar com o banco de dados: {erro}")
        return None, None 
# ---------------------------------------------------------------------------------------------------------------------------------------------

# FUNÇÃO INSERIR TAREFA ----------------------------------------------------------------------------------------
def inserir_tarefa(nome_tarefa,descricao,categoria,data_prazo,prioridade): #PARÂMETROS
    conexao, cursor = conectar() #PARA SE CONECTAR AO BANCO DE DADOS 

    if conexao is None: #VEFIFICA SE A CONEXAO FUNCIONOU, SE NÃO, ELA RETORNA FALSO
        return False
    try:             #PARA COLOCAR NA TABELA DO SCRIPT (INSERIR OS CAMPO DELA)          # %s- bloqueio de segurança de SQL INJECTION
        sql = "INSERT INTO tarefa (nomeTarefa,descricao,categoria,dataPrazo,prioridade) VALUES (%s, %s, %s, %s, %s)" 
       
        cursor.execute(sql, (nome_tarefa,descricao,categoria,data_prazo,prioridade))  #EXECUTAR O  SQL PARAMETIZADO (BLOQUEADO)E PASSA OS PARÂMETROS (BLOQUEIO)
        conexao.commit()  #CONFIRMA AS ALTERAÇÕES
        return True  #RETORNA TRUE PARA FUNÇÃO PRINCIPAL
    except Error as erro:
        print(f"ERRO! Falha ao inserir a tarefa: {erro}")
        return False 
    finally: #FINALIZA FECHANDO O CURSOR
            cursor.close()
            conexao.close()
# ---------------------------------------------------------------------------------------------------------------------------------------------
# FUNÇÃO CONSULTAR TAREFA ----------------------------------------------------------------------------------------
def consultar_tarefas():             #RETORNA TODAS  AS TEREFAS CADASTRADAS NO BANCO DE DADOS 
  
     conexao, cursor = conectar()   #CHAMAR A FUNÇÃO CONECTAR

     if conexao is None:   #SE A CONEXÃO FALHOU 
          return[] #LISTA VAZIA 
     try:   #TENTE EXECUTAR O COMANDO SQL  #SELECIONE TODAS AS COLUNAS DA(ORIGEM) TABELAS
        sql = """
             SELECT 
              idTarefa AS idtarefa, 
              nomeTarefa AS nome_tarefa,
              dataPrazo AS data_prazo,
              status, 
              categoria, 
              descricao, 
              prioridade
             FROM tarefa;

              """   
        cursor.execute (sql)    #EXECUTA O COMANDO DA VARIÁVEL SQL 
        terefas = cursor.fetchall() #BUSCAR TODAS AS LINHAS DA CONSULTA EXECUTADA

        return terefas # RETORNA PARA PROGRAMAÇÃO PRINCIPAL DE TAREFAS 


     except Error as erro:  # SE DER ERRO
            print(f"ERRO! Falha ao listar as tarefas: {erro}")
            return[] # LISTA VAZIA EM CASO DE ERRO 
    
     finally: #FINALIZE SEMPRE 
          cursor.close() #ENCERRA O CURSOR
          conexao.close() #ENCERRA A CONEXAO

# ---------------------------------------------------------------------------------------------------------------------------------------------
# FUNÇÃO CONCLUIR TAREFA ----------------------------------------------------------------------------------------
def concluir_tarefa(idtarefa):
     conexao, cursor = conectar()

     if conexao is None:
          return False
     try:
          sql = "UPDATE tarefa SET status = 'Concluída' WHERE idTarefa = %s"
          cursor.execute(sql,(idtarefa,))
          conexao.commit() #CONFIRMA A ALTERAÇÕES NOS DADOS 
          return True 
          
     except Error as erro:
          print(f"ERRO! Falha ao concluir tarefa: {erro}")
          return False 
          
     finally:
          cursor.close()
          conexao.close()

# ---------------------------------------------------------------------------------------------------------------------------------------------
# FUNÇÃO EDITAR TAREFA ----------------------------------------------------------------------------------------
def alterar_tarefa(idtarefa,nome_tarefa,descricao,categoria,data_prazo,prioridade):
     conexao, cursor = conectar()

     if conexao is None:
          return False
     try:
          sql = "UPDATE tarefa SET nomeTarefa = %s, descricao = %s, categoria = %s, dataPrazo = %s, prioridade = %s WHERE idTarefa = %s"
          cursor.execute(sql,(nome_tarefa, descricao, categoria, data_prazo, prioridade, idtarefa))

          conexao.commit() #CONFIRMA A ALTERAÇÕES NOS DADOS 

          return True 
          
     except Error as erro:
          print(f"ERRO! Falha ao editar a tarefa: {erro}")
          return False 
          
     finally:
          cursor.close()
          conexao.close()

# ---------------------------------------------------------------------------------------------------------------------------------------------
# FUNÇÃO EXCLUIR TAREFA ----------------------------------------------------------------------------------------
def apagar_tarefa(idtarefa):
     conexao, cursor = conectar()

     if conexao is None:
          return False
     try:
          sql = "DELETE FROM tarefa WHERE idTarefa = %s"
          cursor.execute(sql,(idtarefa,))

          conexao.commit() #CONFIRMA A ALTERAÇÕES NOS DADOS 

          return True 
          
     except Error as erro:
          print(f"ERRO! Falha ao excluir a tarefa: {erro}")
          return False 
          
     finally:
          cursor.close()
          conexao.close()
















