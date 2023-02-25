# Desafio: Flask, banco de dados, Docker e Docker Compose
### Objetivo
<p>O objetivo deste desafio é criar uma aplicação web simples de gerenciamento de tarefas (to-do list) usando Python, Flask, banco de dados, Docker e Docker Compose. A aplicação deve permitir que os usuários possam criar, editar e excluir tarefas, bem como marcar tarefas como concluídas.
</p>

### Passos
<p>Para cumprir o objetivo, siga os seguintes passos:</p>

<ol>
  <li>
    Crie o projeto Flask: Crie um projeto Flask simples usando o comando flask init ou flask create-app. Isso irá criar uma estrutura básica do projeto, com um arquivo app.py e um diretório templates e static.
  </li>

  <li>
    Configure o banco de dados: Use o SQLite como banco de dados para este exemplo. Crie uma tabela de tarefas com os seguintes campos: id, title, description, completed. Crie um arquivo database.py para gerenciar a conexão com o banco de dados e definir as funções de CRUD (Create, Read, Update, Delete).
  </li>

  <li>
    Crie as rotas e as views: Crie rotas para as funcionalidades de listar, adicionar, editar e excluir tarefas. Para cada rota, defina uma view correspondente. As views devem se comunicar com o banco de dados para buscar, adicionar, atualizar ou excluir dados.
  </li>

  <li>
    Crie as templates: As templates serão responsáveis por exibir os dados da aplicação para o usuário. Crie templates para listar as tarefas, adicionar uma nova tarefa, editar uma tarefa existente e exibir uma tarefa específica.
  </li>

  <li>
    Configure o Docker e o Docker Compose: Crie um arquivo Dockerfile para configurar a imagem Docker da sua aplicação Flask. Crie também um arquivo docker-compose.yml para orquestrar os containers do seu projeto. Este arquivo incluirá a configuração para o container do banco de dados SQLite.
  </li>

  <li>
    Execute o projeto: Finalmente, execute o projeto usando o comando docker-compose up. Isso iniciará os containers da sua aplicação e do banco de dados, permitindo que você possa acessar a aplicação web em um navegador.
  </li>
</ol>

### Recursos adicionais
<ul>
  <li>
  A documentação oficial do Flask tem um excelente tutorial sobre como integrar o Flask com o SQLite: https://flask.palletsprojects.com/en/2.1.x/tutorial/database/
  </li>

  <li>
  O site Real Python tem uma série de tutoriais sobre Flask, incluindo um tutorial completo sobre como integrar o Flask com o banco de dados MySQL: https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/
  </li>

  <li>
  O site Miguel Grinberg oferece uma série de tutoriais sobre Flask, incluindo um tutorial completo sobre como integrar o Flask com o banco de dados MongoDB: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
  </li>

  <li>
  O canal Corey Schafer no YouTube tem uma série de vídeos sobre Flask, incluindo um tutorial sobre como integrar o Flask com o SQLite: https://www.youtube.com/watch?v=Z1RJmh_OqeA
  </li>
</ul>