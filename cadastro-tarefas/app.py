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
def tasks():
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

@app.route('/task/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def task(id):
  if request.method == 'GET':
    try:
      dados = tarefas[id]
      return jsonify(dados)
    except:
      mensagem = 'Erro na API!'
      return jsonify({"status": "error", "mesagem": mensagem})
  elif request.method == 'PUT':
    dados = json.loads(request.data)
    task = tarefas[id]
    print(task)
    task['status'] = dados['status']
    return jsonify(task)
  elif request.method == 'DELETE':
    tarefas.pop(id)
    return jsonify({"status": "sucesso", "mensagem": "Tarefa deletada com sucesso!"})

if __name__ == '__main__':
  app.run(debug=True)
