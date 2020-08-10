from flask import Flask, request
from flask_restful import Resource, Api
from models import Produtos

app = Flask(__name__)
api = Api(app)

class Produto(Resource):

    #Permiti a vizualização dos dados.
    def get(self, nome):
        produtos = Produtos.query.filter_by(nome=nome).first()
        try:
            response = {
                'ID': produtos.id,
                'nome': produtos.nome,
                'codigo': produtos.codigo,
                'valor': produtos.valor,
                'quantidade': produtos.quantidade
            }
        except AttributeError:
            response = {
                'Status':'ERROR',
                'Mensagem':'PRODUTO NAO ENCONTRADO!'
            }
        return response

    #Permiti fazer alterações nos dados.
    def put(self, nome):
        produtos = Produtos.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            produtos.nome = dados['nome']
        if 'codigo' in dados:
            produtos.codigo = dados['codigo']
        if 'valor' in dados:
            produtos.valor = dados['valor']
        if 'quantidade' in dados:
            produtos.quantidade = dados['quantidade']
        produtos.save()
        response = {
            'ID':produtos.id,
            'nome':produtos.nome,
            'codigo':produtos.codigo,
            'valor': produtos.valor,
            'quantidade': produtos.quantidade
        }
        return response

    #permiti deletar dados.
    def delete(self, nome):
        produtos = Produtos.query.filter_by(nome=nome).first()
        mensagem = 'Produto {} excluido com sucesso'.format(produtos.nome)
        produtos.delete()
        return {'Status': 'Sucesso', 'Mensagem': mensagem}

#Rota:
api.add_resource(Produto, '/produto/<string:nome>/')

#Lista de todos os produtos no bbanco de dados.
class ListaProdutos(Resource):
    # Permiti a inserção de dados.
    def post(self):
        dados = request.json
        produtos = Produtos(nome=dados['nome'], codigo=dados['codigo'], valor=dados['valor'], quantidade=dados['quantidade'])
        produtos.save()
        response = {
            'id': produtos.id,
            'nome': produtos.nome,
            'codigo': produtos.codigo,
            'valor':produtos.valor,
            'quantidade': produtos.quantidade
        }
        return response

    #Mostrar todos os produtos da tabela
    def get(self):
        produtos = Produtos.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'codigo':i.codigo} for i in produtos]
        return response

#Rota:
api.add_resource(ListaProdutos, '/produtos/')

if __name__ == '__main__':
    app.run(debug=True)