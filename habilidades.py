from flask import Flask, request
from flask_restful import Resource
import json

lista_habilidades = ['Python', 'Java', 'Flask', 'PHP']

# devolve uma habilidade pelo ID, também altera e deleta uma habilidade.


class Habilidade(Resource):
    def get(self, id):
        try:
            response = lista_habilidades[id]
        except IndexError:
            mensagem = 'Habilidade de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensgaem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados
        return dados

    def delete(self, id):
        lista_habilidades.pop(id)
        return {'status': 'sucesso', 'mensagem': 'registro excluído'}

# lista todas as habilidades e permite registrar uma nova habilidade


class Habilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)
        posicao = len(lista_habilidades)
        lista_habilidades.append(dados)
        return (lista_habilidades[posicao])
