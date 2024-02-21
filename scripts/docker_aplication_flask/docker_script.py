import docker
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

client = docker.from_env()

# Definindo Dockerfile
dockerfile_content = f'''
FROM python:3.9
WORKDIR /app
COPY app.py /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python3","app.py"]
'''

# Criando o arquivo Dockerfile
dockerfile_path = os.path.join(current_directory, "Dockerfile")
with open(dockerfile_path, "w") as f:
    f.write(dockerfile_content)

# Build da imagem
image, build_logs = client.images.build(path=current_directory, tag="docker-application-flask", rm=True)

# ID da imagem
print(f"ID da imagem: {image.id}")

# Exibindo logs
for log in build_logs:
    print(log)