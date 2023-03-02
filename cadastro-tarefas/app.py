from flask import Flask, jsonify, request
import json

app = Flask(__name__)

tarefas = [
  {
    'id': 0,
    'responsavel': 'João',
    'tarefa': 'Criar um jogo',
    'status': False
  },
  {
    'id': 0,
    'responsavel': 'Luiz',
    'tarefa': 'Criar estrutura inicial',
    'status': True
  }
]

@app.route('/task', methods=['GET', 'POST'])
def get_tasks():
  if request.method == 'GET':
    resp = jsonify(tarefas)
    resp.headers.add('Content-Type', 'application/json')
    return resp
  elif request.method == 'POST':
    print(request.data)
    dados = json.loads(request.data)
    posicao = len(tarefas)
    dados['id'] = posicao
    tarefas.append(dados)
    return jsonify(tarefas[posicao])

if __name__ == '__main__':
  app.run(debug=True)
