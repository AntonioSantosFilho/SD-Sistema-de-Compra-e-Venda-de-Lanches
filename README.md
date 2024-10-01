# Sistema de Venda e Compra de lanches ![WEB](https://img.shields.io/badge/🌐%20WEB-4285F4?style=for-the-badge&logoColor=white)

![Dart](https://img.shields.io/badge/django-%230175C2.svg?style=for-the-badge&logo=django&logoColor=white)
![Flutter](https://img.shields.io/badge/python-%2302569B.svg?style=for-the-badge&logo=python&logoColor=white)


![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-%23000000.svg?style=for-the-badge&logo=linux&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Canva](https://img.shields.io/badge/Canva-%2300C4CC.svg?style=for-the-badge&logo=Canva&logoColor=white)
![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white)


## Passos para Configuração ambiente virtual e dependências 

### 1. Crie um ambiente virtual

Na raiz do projeto, execute o seguinte comando para criar um ambiente virtual utilizando `venv`:

```bash
python -m venv venv
```
Este projeto utiliza um ambiente virtual Python para garantir que as dependências sejam isoladas e gerenciadas adequadamente.



### 2. Ative o ambiente virtual

- **No Windows**:

```bash
venv\Scripts\activate
```

- **No macOS/Linux**:

```bash
source venv/bin/activate
```

Após ativar o ambiente virtual, você deverá ver o nome do ambiente entre parênteses no início do prompt.

### 3. Instale as dependências

Com o ambiente virtual ativo, execute o comando a seguir para instalar as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Ligue o servidor

Execute o seguinte comando para iniciar o servidor:

```bash
python manage.py runserver
```
