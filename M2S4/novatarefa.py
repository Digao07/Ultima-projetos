import sqlite3
conexao = sqlite3.connect ('M2S4.db')

cursor = conexao.cursor()
sql = 'select * from categoria'
consulta = cursor.execute(sql)
for item in consulta:
    print('ID', item[0], 'Categoria', item[1])
categoria_id = input('Digite o ID da categoria para a tarefa: ')
tarefa = input('Digite a tarefa que entrará na lista: ')
hoje = datetime.date.today()
sql_tarefa = 'insert into tarefa (categoria_id, tarefa, data) values (?, ?, ?)'
valores = [categoria_id, tarefa, hoje]
cursor.execute(sql_tarefa, valores)

conexao.commit()
conexao.close()