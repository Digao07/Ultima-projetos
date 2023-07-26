import sqlite3
conexao = sqlite3.connect ('M2S4.db')

cursor = conexao.cursor()
sql_consulta = 'select * from tarefa'
consulta = cursor.execute(sql_consulta)
for item in consulta:
    print('ID', item[0],'Categoria_ID', item[1], 'Tarefa', item[2], 'Data', item[3], 'Status', item[4])
tarefa_id = input('Digite qual o ID da tarefa que deseja deletar: ')
sql_deletar_tarefa = 'delete from tarefa where id = ?'
valores = [tarefa_id]
cursor.execute(sql_deletar_tarefa, tarefa_id)

conexao.commit()
conexao.close()