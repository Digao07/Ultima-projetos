import sqlite3
conexao = sqlite3.connect ('M2S4.db')

cursor = conexao.cursor()
sql_consulta = 'select * from tarefa'
consulta = cursor.execute(sql_consulta)
for item in consulta:
    print('ID', item[0],'Categoria_ID', item[1], 'Tarefa', item[2], 'Data', item[3], 'Status', item[4])
tarefa_id = input('Digite o ID da tarefa: ')
verifica = int(input('Desejas alterar apenas o Status (digite: 1 para sim e 2 para não?) '))
if verifica == 1:
    status = input('Digite o novo status: ')
    sql_status = 'update tarefa set status = ? where id = ?'
    valores = [status, tarefa_id]
    cursor.execute(sql_status, valores)
else:
    sql_consulta_categoria = 'select * from categoria'
    consulta_categoria = cursor.execute(sql_consulta_categoria)
    for item in consulta_categoria:
        print('ID', item[0], 'Categoria', item[1])
    categoria_ID = input('Digite a nova categoria: ')
    tarefa = input('Digite a nova tarefa: ')
    hoje = datetime.date.today()
    status = input('Digite o novo status da tarefa: ')
    sql_update_all = 'update tarefa set categoria_id = ?, tarefa = ?, data = ?, status = ? where id = ?'
    valores = [categoria_ID, tarefa, hoje, status, tarefa_id]
    cursor.execute(sql_update_all, valores)
    
conexao.commit()
conexao.close()