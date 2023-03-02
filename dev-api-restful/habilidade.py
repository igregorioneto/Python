from flask_restful import Resource, Api

lista_habilidades = ['Python', 'Java', 'Flask', 'PHP']

class Habilidades(Resource):
  def get(self):
    return lista_habilidades