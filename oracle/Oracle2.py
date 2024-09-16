import oracledb as oracle

url = "oracle.fiap.com.br/orcl"
con = oracle.connect(user='seu_banco', dsn=url, password='senha_do_seu_banco')
print("Versão do Banco" + con.version)

cur = con.cursor()
sql_lins = '''
    INSERT INTO empregado (nome, cargo, salario, data_contratacao)
    VALUES (:nome, :cargo, :salario, to_date(:data, 'YYYY-MM-DD'))
'''

# Dados a serem inseridos
dado = {
    "nome": "Thiago",
    "cargo": "Ceo",
    "salario": 6000.90,
    "data": "2009-10-23"
}

cur.execute(sql_lins, dado)
con.commit()
cur.close()
con.close()