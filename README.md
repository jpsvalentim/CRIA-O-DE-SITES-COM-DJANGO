# CRIAÇÃO-DE-SITES-COM-DJANGO
Documentação para criar site usando Django.
# 🛠️ Configuração Inicial do Projeto

Este documento orienta os primeiros passos para configurar o ambiente de desenvolvimento deste projeto, que utiliza o framework Django para desenvolvimento web em Python.

---

## 📦 1. Instalação do Anaconda

**Por que usar o Anaconda?**

O [Anaconda](https://www.anaconda.com/) é uma distribuição Python que facilita a gestão de ambientes e pacotes, especialmente útil em projetos que envolvem ciência de dados, desenvolvimento web e outras dependências complexas. Ele já vem com o `conda`, que é uma ferramenta poderosa para criar ambientes isolados com bibliotecas específicas.

**Passos para instalação:**

1. Acesse o site oficial: [https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution)
2. Baixe a versão compatível com seu sistema operacional.
3. Siga o assistente de instalação.
4. Após instalado, abra o terminal ou o Anaconda Prompt.

---

## 🐍 2. Criação de um ambiente virtual com Django

**Por que usar ambientes virtuais?**

Ambientes virtuais permitem que você isole as dependências do projeto atual das de outros projetos. Isso evita conflitos de versão entre bibliotecas e mantém seu sistema organizado.

**Por que usar o Django?**

[Django](https://www.djangoproject.com/) é um framework web de alto nível para Python, que permite o desenvolvimento rápido e seguro de aplicações web. Ele oferece uma estrutura robusta com muitos recursos integrados (ORM, autenticação, painel admin, etc).


## ⚙️ Quem faz o quê?
# 🐍 Anaconda — o ambiente
Anaconda é como uma "caixa de ferramentas + laboratório" para trabalhar com Python.

# No seu projeto, o Anaconda:
📦 Gerencia ambientes virtuais (conda create -n django python=3.x)

🧪 Isola dependências (cada projeto pode ter suas próprias versões de Django, pandas, etc.)

💻 Facilita instalação de pacotes, especialmente os mais complicados como numpy, pandas, matplotlib

🔁 Permite alternar entre projetos sem conflito de versões (conda activate django)

✅ Ele não executa o projeto — ele só prepara o terreno onde o projeto vai rodar.

# 🌐 Django — o motor do site
Django é o framework web em si — o "motor" do seu site.

# No seu projeto, o Django:
🧠 Gerencia toda a lógica do seu site (rotas, banco de dados, autenticação)

📄 Cria páginas, APIs, sistemas administrativos

📂 Organiza a estrutura do projeto (apps, templates, modelos)

🚀 Roda o servidor de desenvolvimento com manage.py runserver

✅ Ele é quem roda o projeto, cria o site e interage com o navegador.

## 🧠 Analogia simples:
# Papel	                                                       Quem?
🧰 Ferramenta que instala e organiza                   o ambiente	Anaconda
🏗️ Framework que constrói o site/app	                      Django



**Criando o ambiente:**

# Abra o terminal (ou Anaconda Prompt) e execute:
>>> bash
conda create -n meuambiente-django python=3.11

# Ative o ambiente:
>>> bash
conda activate meuambiente-django

# Instale o Django:
>>> bash
pip install django

# Verifique a instalação:

>>>bash
django-admin --version

---

## 💻 3. Escolha e Instalação de um Editor de Código

Para desenvolver com mais eficiência, é altamente recomendado o uso de um editor de código moderno com suporte a Python e ao framework Django. As duas opções mais populares são:

### 🔷 PyCharm

**Por que usar o PyCharm?**

O [PyCharm](https://www.jetbrains.com/pycharm/) é um IDE completo para desenvolvimento em Python, com suporte nativo a Django. Ele oferece:

- Autocompletar avançado
- Debugger visual
- Gerenciador de pacotes integrado
- Suporte completo a templates, models, views e rotas do Django

**Instalação:**

1. Acesse: [https://www.jetbrains.com/pycharm/download](https://www.jetbrains.com/pycharm/download)
2. Escolha a versão **Community** (gratuita) ou **Professional** (paga, com mais recursos para Django).
3. Siga o assistente de instalação conforme seu sistema operacional.

---

### 🟦 Visual Studio Code (VS Code)

**Por que usar o VS Code?**

O [VS Code](https://code.visualstudio.com/) é um editor de código leve, altamente customizável e com uma grande variedade de extensões. Para projetos Django, é uma ótima opção por ser rápido e prático, além de consumir menos recursos que um IDE completo como o PyCharm.

**Instalação:**

1. Acesse: [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Baixe e instale a versão para seu sistema.
3. Após instalado, adicione as extensões recomendadas:

    - **Python** (Microsoft)
    - **Django** (BAT)
    - **Pylance** (para sugestões e análise de código)
    - **Prettier** ou **Black** (para formatação de código)

---

## ✅Recomendações:
> - Se você está começando e quer algo mais completo, vá de **PyCharm**.
> - Se prefere leveza e customização, **VS Code** é uma excelente escolha.


## 📁 Estrutura do seu projeto:
CRIA-O-DE-SITES-COM-DJANGO/
    📁 meusite/
        📁 meusite/
            📄 __init__.py
            📄 settings.py
            📄 urls.py
            📄 wsgi.py
            📄 asgi.py
        📄 manage.py
        📄 db.sqlite3
    📄 README.md


## 🧠 Explicação de cada um:
🔹 manage.py
Arquivo de linha de comando do Django. Você usa ele pra rodar o servidor, criar apps, aplicar migrações etc.

Ex: python manage.py runserver, python manage.py startapp nome.

🔹 db.sqlite3
Banco de dados SQLite padrão do Django. Criado automaticamente quando você roda runserver pela primeira vez ou faz migrações.

## 📁 meusite (a pasta interna)
Esse é o módulo principal do seu projeto. O nome pode confundir porque se repete, mas é normal. Dentro dela estão arquivos que controlam a configuração geral do Django:

## 🔸 __init__.py
Diz ao Python que essa pasta é um módulo. Sem isso, o Django não consegue importar corretamente.

## 🔸 settings.py
Onde ficam as configurações do projeto:

Idioma, fuso horário

Quais apps estão instalados

Banco de dados

Pastas de arquivos estáticos e templates

## 🔸 urls.py
Responsável por mapear as rotas (URLs) do seu site.

Exemplo: /admin/, /meusite/, etc.

## 🔸 wsgi.py
Usado para deploy (colocar o site no ar com servidores como Gunicorn/Apache).

Aponta para a aplicação Django.

## 🔸 asgi.py
Como o wsgi.py, mas para servidores assíncronos (Ex: WebSockets, Channels).

Importante para aplicações em tempo real.

## 🔸 README.md
Arquivo comum em projetos para explicar o que é o projeto, como rodar, requisitos, etc.
