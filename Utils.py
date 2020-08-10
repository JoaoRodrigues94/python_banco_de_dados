from models import Produtos

#Insere dados na tabela produtos
def adicionar():
    produto = Produtos(nome='B', codigo='1A', valor=10.00, quantidade=3)
    print(produto)
    produto.save()

#Realiza a pesquisa de todos os dados contidos na tabela produtos.
def pesquisar_todos():
    produto = Produtos.query.all()
    print(produto)

#Pesquisa apenas um dado especifico.
def pesquisar_especifico():
    produto = Produtos.query.filter_by(nome='C').first()
    print(produto.codigo)

#Permiti fazer alterações em determinado dado
def alterar():
    produto = Produtos.query.filter_by(nome='C').first()
    produto.codigo = '45'
    produto.save()

#Exclusão de um dado na tabela produtos
def deletar():
    produto = Produtos.query.filter_by(nome='A').first()
    produto.delete()
    print('Produto deletado com sucesso!')


if __name__ == '__main__':
    #adicionar()
    #alterar()
    #deletar()
    pesquisar_todos()
    #pesquisar_especifico()