import docker

# Criar cliente docker
client = docker.from_env()

# Definindo as configurações da imagem
dockerfile_content = '''
FROM alpine:latest
RUN apk update && apk add python3
CMD ["python3", "-c", "print('Hello, Docker!')"]
'''

# Criando arquivo Dockerfile
with open('Dockerfile', 'w') as f:
    f.write(dockerfile_content)

# Construindo a imagem
image, build_logs = client.images.build(path='.', tag='hello-docker', rm=True)

# Exibe o ID da Imagem
print(f"ID da imagem: {image.id}")

# Exibindo logs de construção
for log in build_logs:
    print(log)