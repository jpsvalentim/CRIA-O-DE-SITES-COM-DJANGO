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
