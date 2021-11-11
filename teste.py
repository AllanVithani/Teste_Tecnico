import requests
import psycopg2
import sys
import json


#configuração BD 
host = 'localhost'
dbname = 'teste_alfa'
user = 'postgres'
password = 'root'

#String de conec
conn_string =  'host={0} user={1} dbname={2} password={3} '.format(host, user, dbname, password)
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()



def Requisicao_cnpj():
    cnpj = input ("Digite o CNPJ que deseja consultar: ")
    r = requests.get("https://www.receitaws.com.br/v1/cnpj/"+cnpj)
    r = r.json() 
    status = r['status']      
        
    if status == '200':
            verificacao = input("Digite 'sim' para inserir os dados no banco ou 'nao' para sair:\n")
            if verificacao == "sim":
                    cnpj_insert = r['cnpj']
                    nome_filial = r['nome']
                    cidade_filial = r['municipio']
                    estado = r['uf']
                    cursor.execute("INSERT INTO Filiais(CNPJ, nome, cidade, estado) VALUES ('"+cnpj_insert+"','"+nome_filial+"',"+"'"+cidade_filial+"',"+"'"+estado+"')")
                    conn.commit()
                    cursor.close
                    conn.close
                    print("Dados inseridos com sucesso!")
            elif verificacao == "nao":
                    print ("deu boa")

            else:
                    print("opção inválida")
    elif status == '404' or 'ERROR':
            print("CNPJ inválido!")  
    else:
            print("Tivemos um problema para encontrar o CNPJ")


op = input("Digite a opção desejada: \n1 - Consulta CNPJ  \n2 - Inserir dados de Filial Manualmente \n3 - Deletar dados de Filial \n4 - Atualizar dados da Filial \n")

def switch(op):
    if op == "1":
       return Requisicao_cnpj()
    elif op == "2":
        print("Em desenvolvimento")
        
    elif op == "3":
        print("Em Desenvolvimento")
    elif op == "4":
        print("Em Desenvolvimento")
    else:
        print("Escolha uma opção válida")

if __name__ == "__main__":
    function = switch(op)
    function