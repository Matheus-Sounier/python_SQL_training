import oracledb
from decouple import config

with oracledb.connect(
    user = config('PYTHON_USER'),
    password = config('PYTHON_PWD'),
    dsn = config('PYTHON_DSN')
) as conn:
    with conn.cursor() as cursor:
        cursor.execute('SELECT id, nome FROM setores')
        linhas = cursor.fetchall()
        for row in linhas:
            print(row)
        
        # cursor.execute('select nome, pais from fornecedores')
        # linhas_fodas = cursor.fetchall()
        # for row in linhas_fodas:
        #     print(row)

        cursor.execute('select s.nome, e.quantidade, e.minimo from estoque e join setores s on s.id = e.setor_id')
        isso_ai = cursor.fetchall()
        for i in isso_ai:
            print(i)
