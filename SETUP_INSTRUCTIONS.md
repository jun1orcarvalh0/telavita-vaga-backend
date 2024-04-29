# Documentação

## Sobre o projeto:
 * O projeto foi desenvolvido utilizando a arquitetura de apps (models, serializers e views) do Django. A única app criada é a departments que envolve tanto os departamentos (departments) quanto os colaboradores de um departamento (employees)
 * Optei por deixar tudo em uma mesma app porque o projeto era pequeno e não dependia de outras models ou regras de negócio. Contudo, poderíamos ter duas apps separadas (departmens e employees).
 * A referência com SwaggerUI está disponível na rota docs/swagger

## Configuração e Inicialização:
Para rodar o sistema localmente será necessário ter na máquina o [Docker](https://www.docker.com/), todo o processo de configuração do Docker poderá ser encontrado no site oficial.

Com o Docker instalado e configurado, execute o seguinte comando:
 ```bash
docker-compose up --build
```
Caso já tenha rodado o comando acima e queira rodar o ambiente em segundo plano:
  ```bash
docker-compose up -d
  ```

## Rodar os testes:
Para rodar os testes você deve primeiramente entrar no container app (certifique-se de estar na pasta principal do projeto):
 ```bash
docker exec -it app sh
```

Para rodar todos os testes da app departments execute o comando:
 ```bash
python manage.py test
```
