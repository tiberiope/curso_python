import sqlite3

conexao = sqlite3.connect('aula44.db')
c = conexao.cursor()

c.execute('CREATE TABLE IF NOT EXISTS usuario(id integer, nome text)')

c.execute("INSERT INTO usuario VALUES (1, 'Artur')")
c.execute("INSERT INTO usuario VALUES (2, 'Rodrigo')")
c.execute("INSERT INTO usuario VALUES (3, 'Pedro')")

#conexao.commit()

requisicao = 'SELECT * FROM usuario WHERE nome = ?'

for linha in c.execute(requisicao, ('Artur',)):
    print(linha)