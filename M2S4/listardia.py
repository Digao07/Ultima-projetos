import sqlite3
conexao = sqlite3.connect ('M2S4.db')

cursor = conexao.cursor()
dia = input('Digite o dia que deseja verificar: (AAAA-MM-DD) ')
sql = 'select * from tarefa where data = ?'
valores = [dia]
consulta = cursor.execute(sql, valores)
for item in consulta:
    print('ID', item[0], 'Tarefa', item[2])
    
conexao.commit()
conexao.close()