# DistribuLanche 🍔🍟
<br><br>
### *Descentralizado no sistema, unificado no sabor!*


<br><br><br><br>


[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![Visual Studio Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Canva](https://img.shields.io/badge/Canva-00C4CC?style=for-the-badge&logo=canva&logoColor=white)](https://www.canva.com/)
[![Google Cloud](https://img.shields.io/badge/Google%20Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![AJAX](https://img.shields.io/badge/AJAX-0078D4?style=for-the-badge&logo=ajax&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/Guide/AJAX)
[![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)](https://www.postman.com/)

---



## 📑 Apresentação do Projeto

<a href="https://github.com/AntonioSantosFilho/SD-Sistema-de-Compra-e-Venda-de-Lanches/blob/main/images.to.github/Distribulanche%20-%20Apresenta%C3%A7%C3%A3o%20projeto.pdf" target="_blank">
    <img src="https://img.shields.io/badge/Abrir%20Apresentação-PDF-blue?style=for-the-badge&logo=adobeacrobatreader&logoColor=white" alt="Ler Apresentação do projeto">
</a>
<br><br>

O **Distribulanche** é uma aplicação desenvolvida como parte da disciplina de **Sistemas Distribuídos** na **UNIVASF**. Ela foi projetada para conectar vendedores e compradores de lanches de maneira eficiente e organizada. 

Diante da proibição de vendas espontâneas nos corredores do campus, a plataforma surge como uma solução inovadora para permitir que vendedores cadastrem produtos e usuários realizem compras de forma centralizada.

---

## 🖼️ **Demonstração do Projeto**

### Interface do Sistema:

| ![Tela 7](https://github.com/AntonioSantosFilho/SD-Sistema-de-Compra-e-Venda-de-Lanches/blob/main/images.to.github/7.png) | ![Tela 8](https://github.com/AntonioSantosFilho/SD-Sistema-de-Compra-e-Venda-de-Lanches/blob/main/images.to.github/8.png) | ![Tela 6](https://github.com/AntonioSantosFilho/SD-Sistema-de-Compra-e-Venda-de-Lanches/blob/main/images.to.github/6.png) |
|:---------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| ![Tela 1](https://github.com/AntonioSantosFilho/SD-Sistema-de-Compra-e-Venda-de-Lanches/blob/main/images.to.github/1.png) | ![Tela 2](https://github.com/AntonioSantosFilho/SD-Sistema-de-Compra-e-Venda-de-Lanches/blob/main/images.to.github/2.png) | ![Tela 3](https://github.com/AntonioSantosFilho/SD-Sistema-de-Compra-e-Venda-de-Lanches/blob/main/images.to.github/3.png) |
| ![Tela 4](https://github.com/AntonioSantosFilho/SD-Sistema-de-Compra-e-Venda-de-Lanches/blob/main/images.to.github/4.png) | ![Tela 5](https://github.com/AntonioSantosFilho/SD-Sistema-de-Compra-e-Venda-de-Lanches/blob/main/images.to.github/5.png) |                                                                                   |

---





## 🛠️ **Tecnologias Utilizadas**

Este projeto utiliza as seguintes tecnologias:

- **Backend**: Django
- **Frontend**: Django Templates
- **Banco de Dados**: PostgreSQL
- **Ambiente**: Docker e Docker Compose
- **Ferramentas de Desenvolvimento**: Git e Visual Studio Code
- **Design de Interface**: Canva
- **Outras Tecnologias**: Google Cloud, AJAX, Bootstrap...

---



## 🎨 **Identidade Visual**

- **Cores**:
  - #8c0234
  - #fc7c0f
- **Fonte da Logo**:
  *Euphoria Script*



---

## 📋 **Funcionalidades do Sistema**

### **Principais Funcionalidades**
1. **Vendedores**:
   - Cadastrar produtos e definir horários de disponibilidade.
   - Gerenciar pedidos e responder a mensagens no chat.
2. **Usuários**:
   - Visualizar catálogo de produtos.
   - Realziar compras.
   - Avaliar compras.
   - Comunicação direta com vendedores via chat.

### **Requisitos Obrigatórios**
- Customização do Admin Django.
- Autenticação e recuperação de senha.
- Validação de dados e envio de e-mails.
- Banco de dados robusto com:
  - 8 tabelas principais.
  - 5 tabelas auxiliares.
- Framework de mensagens e paginação.

### **Requisitos Desejáveis**
- Integração com Mercado Pago para pagamentos via API REST.
- Fornecimento de API para consumo de recursos por outros sistemas.

---

## ⚠️ **Observações**

Para garantir a segurança e a privacidade dos dados, algumas informações sensíveis foram removidas deste repositório. Isso inclui:

- **Chaves de API** do **Mercado Pago**.
- **Senhas de aplicativos SMTP** utilizados para envio de e-mails, como o **Google App Password**.

Caso precise executar o projeto em ambiente local, você deverá configurar essas credenciais manualmente em arquivos apropriados, como o `.env`. Essas informações devem ser obtidas diretamente nas plataformas correspondentes:

- A chave de API do **Mercado Pago** pode ser gerada na [plataforma Mercado Pago](https://www.mercadopago.com.br/).
- A senha de aplicativo SMTP do **Google** pode ser configurada na [Central de Segurança do Google](https://myaccount.google.com/security).

Recomendamos que **não compartilhe essas credenciais publicamente** para evitar problemas de segurança.


---
## 🚀 **Instruções de Instalação e Uso**

### **1️⃣ Ambiente Local**

#### **Pré-requisitos**
- Certifique-se de ter as seguintes ferramentas instaladas:
  - **Docker** e **Docker Compose**
  - **Python 3.10+**
  - **Git**

#### **Passos para Configuração**

1. **Clone o Repositório**
   ```bash
   git clone https://github.com/seu-usuario/distribulanche.git
   cd distribulanche
   ```

2. **Configure os Domínios Locais**
   Adicione os seguintes domínios ao arquivo `/etc/hosts`:
   ```
   127.0.0.1 projetosd.local
   127.0.0.1 www.projetosd.local
   127.0.0.1 adm.projetosd.local
   127.0.0.1 api.projetosd.local
   ```

3. **Inicialize o Banco de Dados**
   Execute o script de inicialização do banco:
   ```bash
   sh init_db.sh
   ```

4. **Suba os Contêineres**
   Inicie os serviços com Docker Compose:
   ```bash
   docker compose up -d
   ```

5. **Configure o Django**
   Realize as migrações e crie o superusuário:
   ```bash
   docker exec -it web python manage.py makemigrations
   docker exec -it web python manage.py migrate
   docker exec -it web python manage.py createsuperuser
   ```

6. **Acesse os Serviços Locais**
   Utilize os seguintes endereços no navegador:
   - **Frontend**: `https://projetosd.local`
   - **Administração Banco dados**: `https://adm.projetosd.local`
   - **API**: `https://api.projetosd.local`

---

### **2️⃣ Ambiente Remoto**

#### **Pré-requisitos**
- Criar uma instância de máquina virtual (VM) em uma nuvem de sua preferência (AWS, GCP, Azure, etc.).
- Configurar a conectividade via SSH.

#### **Passos para Configuração**

1. **Crie Chaves SSH**
   Gere suas chaves SSH localmente:
   ```bash
   ssh-keygen -t rsa -f projetosd.pem -C "seu-email@exemplo.com" -b 2048
   ```

2. **Configure a Instância**
   - Adicione a chave pública à configuração da VM.
   - Faça login na instância via SSH:
     ```bash
     ssh -i projetosd.pem usuario@<ip-da-instancia>
     ```

3. **Clone o Repositório**
   ```bash
   git clone https://github.com/seu-usuario/distribulanche.git
   cd distribulanche
   ```

4. **Prepare o Ambiente**
   - Crie a pasta `/secrets` e adicione as variáveis no arquivo `.env.prod`.
   - Configure senhas seguras para produção.

5. **Inicialize os Serviços**
   Inicie os contêineres Docker:
   ```bash
   docker compose up -d
   ```

6. **Configure os Domínios Remotos**
   Configure os domínios públicos para os serviços, como:
   - **Frontend**: `https://www.projetosd.com.br`
   - **Administração**: `https://adm.projetosd.com.br`
   - **API**: `https://api.projetosd.com.br`

7. **Acesse os Serviços Remotos**
   Utilize os endereços configurados no domínio remoto.

---



## 👥 **Contribuidores**

Projeto desenvolvido por estudantes da **UNIVASF** como parte da disciplina de **Sistemas Distribuídos**:

- **[Antonio](https://github.com/AntonioSantosFilho)**
- **[Andréa](https://github.com/andrea-enginner)**
- **[João Pedro](https://github.com/Sansaocarrasco)**
---

## 🛡️ **Licença**

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT). Sinta-se à vontade para usar, modificar e distribuir!

---

## 🌟 **Agradecimentos**

Agradecemos à **UNIVASF** e ao professor Jairson Rodrigues, responsável pela disciplina de **Sistemas Distribuídos** por nos proporcionar a oportunidade de desenvolver este projeto.

---
