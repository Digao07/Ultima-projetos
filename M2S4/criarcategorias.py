import sqlite3
conexao = sqlite3.connect ('M2S4.db')

cursor = conexao.cursor()

categoria = input('Digite a descrição da categoria: ')

sql = 'insert into categoria (categoria) values (?)'

valores = [categoria]

cursor.execute(sql, valores)

conexao.commit()

conexao.close()