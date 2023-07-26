import sqlite3
conexao = sqlite3.connect ('M2S4.db')

cursor = conexao.cursor()
sql_categoria = 'select id, categoria from categoria'
consulta = cursor.execute(sql_categoria)
for item in consulta:
    print("ID:", item[0], "Categoria:", item[1])
categoria_id = input('Digite qual o ID da categoria que deseja atualizar: ')
sql_deletar_categoria = 'delete from categoria where id = ?'
valores = [categoria_id]
cursor.execute(sql_deletar_categoria, categoria_id)

conexao.commit()
conexao.close()