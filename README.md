# Projeto_Ceos
Considerando que você ja possui conhecimentos de docker, para subir o container:
- docker compose build
- docker compose up
(caso queira especificar, use: "api" e "db" como parametros)

Depois de subir o container, o servidor deverá estar no ar automaticamente.

ACESSE: http://0.0.0.0:8000/docs para testar os metodos da api.


DESCRIÇÃO:
Essa api gerencia um banco de dados, com a tabela "skills".
Skills (habilidades) são poderes especiais que um personagem de um jogo de RPG pode ter.

Por exemplo, um personagem pode possuir a skill "Aumento de velocidade",
que dá a ele a capacidade de correr duas vezes mais rapido por 10 minutos.

Essa api permite ler, criar, atualizar e deletar skills da tabela "skills".

Cada skill possui 3 atributos:
- id: numero que identifica a skill (cada id é único)
- skill_name: o nome da skill
- description: a descrição dos efeitos da skill

Exemplos de skills:
[
    {
         "skill_name": "Corpo de ferro",
         "id": 1,
         "description": "Deixa o corpo do usuário tão resistente quanto ferro"
    },
    {
        "skill_name": "Pensamento paralelo",
        "id": 2,
        "description": "Cria na sua mente uma copia sua que consegue pensar de maneira independente. Em outras palavras, cria um clone da sua mente."
    },
    {
        "skill_name": "Síntese de veneno",
        "id": 3,
        "description": "Permite ao usuario produzir veneno no seu corpo, que pode ser liberado pelos poros das mãos. (O usuario é imune ao proprio veneno)"
    }
]


METODOS:

∙ GET:

- Read skills:
Lê as skills presentes na tabela, organizado-as por id em ordem crescente.
Recebe como parâmetros:
skip (número que diz quantas skills do começo da lista você não quer que apareçam)
limit (número que limita a qauntidade de skills que devem ser lidas)

- Read skill:
Recebe o id de uma skill como parâmetro e retorna todas as informações dela.


∙ POST:

- Create skill: Cria uma nova skill na tabela.
Você deve enviar o nome da skill e a descrição das suas habilidades.


∙ PUT:

- Update skill name: Atualiza o nome de uma skill.
Recebe o id da skill como parâmetro.

- Update skill description: Atualiza a descrição de uma skill.
Recebe o id da skill como parâmetro.


∙ DELETE:

- Delete skill: Apaga uma skill da tabela.
Recebe o id da skill como parâmetro.
