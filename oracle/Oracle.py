import oracledb as banco
url = "oracle.fiap.com.br/orcl"

conn = banco.connect(user='rm557992', password='240504', dsn=url)
print("Versão do Banco" + conn.version)

curso = conn.cursor()
curso.execute('SELECT * FROM dept')
reg = curso.fetchall()
print("Tipo de objeto retornado:", type(reg))

for info in reg:
    print(info)



curso.close()
conn.close()

