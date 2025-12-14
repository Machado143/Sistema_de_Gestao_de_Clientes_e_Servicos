# Sistema de Gestão de Clientes e Serviços

[![Django](https://img.shields.io/badge/Django-4.2-green)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📋 Descrição

O **Sistema de Gestão de Clientes e Serviços** é uma aplicação web desenvolvida em Django para gerenciar ordens de serviço, clientes, serviços e status de forma eficiente. Ideal para assistências técnicas, oficinas e empresas de manutenção que precisam organizar solicitações de serviço, rastrear o progresso e gerar relatórios.

### Funcionalidades Principais
- **Gestão de Ordens de Serviço**: Crie, edite, exclua e visualize detalhes de ordens com filtros por busca e status.
- **Cadastro de Clientes**: Registre e gerencie informações de clientes (nome, email, telefone).
- **Catálogo de Serviços**: Cadastre serviços com descrição e preço, e associe-os às ordens.
- **Status Personalizáveis**: Defina status como "Pendente", "Em Andamento" e "Concluída" para rastrear o progresso.
- **Dashboard com Estatísticas**: Visão geral com totais de ordens, clientes, receita, ordens recentes, pendentes e gráficos mensais.
- **Paginação e Busca**: Navegação paginada em listas e filtros de busca para melhor usabilidade.
- **Exportação CSV**: Exporte dados de ordens para análise externa.
- **Validações Customizadas**: Verificações de integridade de dados, como data de conclusão obrigatória para status "Concluída".
- **Interface Responsiva**: Design moderno e responsivo com navegação intuitiva.

## 🛠️ Tecnologias Utilizadas
- **Backend**: Django 4.2, Python 3.11
- **Banco de Dados**: SQLite (padrão do Django, fácil migração para PostgreSQL/MySQL)
- **Frontend**: HTML5, CSS3, Bootstrap-like styles (custom CSS)
- **Outras**: Django Forms, Django Messages, Paginação nativa

## 📦 Instalação

### Pré-requisitos
- Python 3.11 ou superior
- Git instalado

### Passos para Instalação
1. **Clone o Repositório**:
   ```
   git clone https://github.com/seu-usuario/sistema-assistencia.git
   cd sistema-assistencia
   ```

2. **Crie um Ambiente Virtual**:
   ```
   python -m venv .venv
   # No Windows:
   .venv\Scripts\activate
   # No Linux/Mac:
   source .venv/bin/activate
   ```

3. **Instale as Dependências**:
   ```
   pip install -r requirements.txt
   ```
   *Nota: Se não houver requirements.txt, instale Django manualmente: `pip install django==4.2`*

4. **Configure o Banco de Dados**:
   ```
   cd assistencia
   python manage.py migrate
   ```

5. **Crie um Superusuário** (para acesso admin):
   ```
   python manage.py createsuperuser
   ```

6. **Execute o Servidor de Desenvolvimento**:
   ```
   python manage.py runserver
   ```

7. **Acesse a Aplicação**:
   - Abra o navegador em `http://127.0.0.1:8000/`
   - Para o painel admin: `http://127.0.0.1:8000/admin/`

### Configuração Adicional
- **Email**: Configure as configurações de email em `assistencia/settings.py` se necessário (para notificações).
- **Produção**: Para deploy em produção, configure um servidor WSGI (Gunicorn), banco de dados real e variáveis de ambiente para SECRET_KEY.

## 🚀 Uso

1. **Login**: Use as credenciais do superusuário criado.
2. **Navegação**: Acesse o Dashboard para visão geral ou as seções de Ordens, Clientes, Serviços e Status.
3. **Gerenciamento**:
   - Crie novas ordens selecionando cliente, serviço e status.
   - Busque e filtre listas para encontrar registros rapidamente.
   - Exporte dados via CSV para relatórios.
4. **Validações**: O sistema valida automaticamente campos obrigatórios e regras de negócio (ex: data de conclusão para ordens concluídas).

### Exemplo de Fluxo
- Cadastre um cliente em "Clientes > Novo".
- Crie um serviço em "Serviços > Novo".
- Crie uma ordem em "Ordens > Nova", associando cliente e serviço.
- Atualize o status e adicione data de conclusão quando finalizado.

## 📊 Dashboard
O dashboard exibe:
- Totais de ordens, clientes e serviços.
- Distribuição de ordens por status.
- Receita total e mensal.
- Ordens recentes e pendentes.
- Top 5 clientes e serviços mais utilizados.


## 🤝 Contribuição

Contribuições são bem-vindas! Siga estes passos:

1. Fork o projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`).
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`).
4. Push para a branch (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.

### Padrões de Código
- Siga PEP 8 para Python.
- Use nomes descritivos em inglês/português consistente.
- Adicione testes unitários para novas features.

