import oracledb
from decouple import config

with oracledb.connect(
    user = config('PYTHON_USER'),
    password = config('PYTHON_PWD'),
    dsn = config('PYTHON_DSN')
) as conn:
    with conn.cursor() as cursor:
        # cursor.execute('SELECT id, nome FROM setores')
        # linhas = cursor.fetchall()
        # for row in linhas:
        #     print(row)
        
        # cursor.execute('drop view vw_produto_fornecedor')
        cursor.execute('create or replace view vw_produto_fornecedor as select f.nome, p.descricao, p.preco_unitario from produtos p join fornecedores f on f.id = p.fornecedor_id')
        cursor.execute('select * from vw_produto_fornecedor where preco_unitario > (select avg(preco_unitario) from produtos)')
        produto_fornecedor = cursor.fetchall()
        for i in produto_fornecedor:
            print(produto_fornecedor)
        # for nome, descricao, preco_unitario in produto_fornecedor:
        #     print(f'Empresa: {nome} | Produto: {descricao} | Preço Únitario: {preco_unitario}')

        # cursor.execute('select * from vw_produto_fornecedor')
        # faz = cursor.fetchmany(5)
        # for codigo, descricao, categoria, nome, pais in faz:
        #     print(f'Nome_empresa: {nome} | Empresa_pais: {pais} | Código: {codigo} | Produto: {descricao} | Categoria: {categoria}')
        
        # cursor.execute('select nome, pais from fornecedores')
        # linhas_fodas = cursor.fetchall()
        # for row in linhas_fodas:
        #     print(row)

        # cursor.execute('select s.nome, e.quantidade, e.minimo from estoque e join setores s on s.id = e.setor_id')
        # isso_ai = cursor.fetchall()
        # for nome, quantidade, minimo in isso_ai:
        #     print(f"Setor: {nome} | Qtd: {quantidade} | Mínimo: {minimo}")

        # cursor.execute('create or replace view vw_')
